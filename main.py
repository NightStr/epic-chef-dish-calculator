import csv
import itertools

from pydantic import BaseModel

from calculations.calculator import EpicChefCalculator
from dish.base import BaseIngredient
from dish.ingredients import *
from dish.sauces import *


class CalculationResult(BaseModel):
    ingredients: List[BaseIngredient]
    points: BasePoint
    points_sum: float


def calculate_points(player_level: int, ingredients: List[Ingredient], sauces: List[Sauce]) -> List[CalculationResult]:
    calculations_result = []
    for ingredients_combination in itertools.combinations(ingredients, 3):
        for sauce in sauces:
            list_ingredients = list(ingredients_combination)
            list_ingredients.append(sauce)
            for combination in itertools.combinations(list_ingredients, 4):
                print(f"Вычисление для {combination}.")
                r = EpicChefCalculator().calculate(player_level, list(combination))
                print(f"Результат для {combination}: {r}")
                calculations_result.append(CalculationResult(
                    ingredients=list(combination),
                    points=r,
                    points_sum=r.vgr+r.sprt+r.soph
                ))
    return calculations_result


if __name__ == "__main__":
    all_ingredients = [i() for i in Ingredient.__subclasses__()]
    all_sauces = [s() for s in Sauce.__subclasses__()]
    player_level = int(input("Уровень игрока: "))
    r = calculate_points(player_level, all_ingredients, all_sauces)
    with open("calculation_result.csv", "w+") as f:
        fieldnames = ["Ингридиент_1", "Ингридиент_2", "Ингридиент_3", "Ингридиент_4", "vgr", "sprt", "soph",
                      "Сумма баллов"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for calculation_result in sorted(r, key=lambda cr: cr.points_sum, reverse=True):
            writer.writerow({
                "Ингридиент_1": calculation_result.ingredients[0],
                "Ингридиент_2": calculation_result.ingredients[1],
                "Ингридиент_3": calculation_result.ingredients[2],
                "Ингридиент_4": calculation_result.ingredients[3],
                "vgr": calculation_result.points.vgr,
                "sprt": calculation_result.points.sprt,
                "soph": calculation_result.points.soph,
                "Сумма баллов": calculation_result.points_sum
            })
