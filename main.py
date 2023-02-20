import itertools
import sqlite3
from time import sleep
from typing import Generator

from pydantic import BaseModel

from calculations.calculator import EpicChefCalculator
from dish.base import BaseIngredient
from dish.ingredients import *
from dish.sauces import *


class CalculationResult(BaseModel):
    ingredients: List[BaseIngredient]
    points: BasePoint
    points_sum: float


def calculate_points(player_level: int, ingredients: List[Ingredient], sauces: List[Sauce]) -> Generator[CalculationResult, None, None]:
    c = 0
    for ingredients_combination in itertools.product(ingredients, repeat=3):
        for sauce in sauces:
            list_ingredients = list(ingredients_combination)
            list_ingredients.append(sauce)
            for combination in set(itertools.permutations(list_ingredients, 4)):
                r = EpicChefCalculator().calculate(player_level, list(combination))
                yield CalculationResult(
                    ingredients=list(combination),
                    points=r,
                    points_sum=r.vgr+r.sprt+r.soph
                )
                c += 1
        print(f"{c} из 36925056")


if __name__ == "__main__":
    all_ingredients = [i() for i in Ingredient.__subclasses__()]
    all_sauces = [s() for s in Sauce.__subclasses__()]
    player_level = int(input("Уровень игрока: "))

    # Подключаемся к базе данных или создаем ее, если она не существует
    conn = sqlite3.connect('epic-chef.db')

    # Создаем курсор для выполнения запросов к базе данных
    cursor = conn.cursor()

    # Создаем таблицу
    cursor.execute('''DROP TABLE IF EXISTS dishes''')
    cursor.execute('''CREATE TABLE dishes
                      (ingredient_1 TEXT, ingredient_2 TEXT, ingredient_3 TEXT, ingredient_4 TEXT,
                      vgr REAL, sprt REAL, soph REAL, required_level int, sum_points REAL)''')
    c = 0
    for r in calculate_points(player_level, all_ingredients, all_sauces):
        levels = []
        for i in r.ingredients:
            for s in i.synergies:
                levels.append(s.min_level)
        min_level_required = max(levels) if levels else 0
        cursor.execute(
            f"INSERT INTO dishes VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                str(r.ingredients[0]), str(r.ingredients[1]), str(r.ingredients[2]), str(r.ingredients[3]),
                r.points.vgr, r.points.sprt, r.points.soph, min_level_required, r.points_sum
            )
        )
        c += 1

        if c == 50_000:
            c = 0
            for i in range(10):
                try:
                    conn.commit()
                except Exception as e:
                    print(f"Failed to write into db due error {e}")
                    sleep(2*i)
                else:
                    break

    cursor.execute("CREATE INDEX sum_points_index ON dishes('sum_points')")
    cursor.execute("CREATE INDEX required_level_index ON dishes('required_level')")
    cursor.execute("CREATE INDEX ingr1_index ON dishes('ingredient_1')")
    cursor.execute("CREATE INDEX ingr2_index ON dishes('ingredient_2')")
    cursor.execute("CREATE INDEX ingr3_index ON dishes('ingredient_3')")
    cursor.execute("CREATE INDEX ingr4_index ON dishes('ingredient_4')")
    conn.commit()
    conn.close()
