import itertools
import os
from typing import Generator

from pydantic import BaseModel
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from tqdm import tqdm

from calculations.calculator import EpicChefCalculator
from dish.base import BaseIngredient
from dish.ingredients import *
from dish.sauces import *
import models


CACHE_CHUNK_SIZE = 500_000

engine = create_engine('sqlite:///epic-chef.db')
Session = sessionmaker(bind=engine)
session = Session()


class CalculationResult(BaseModel):
    ingredients: List[BaseIngredient]
    points: BasePoint
    points_sum: float


def get_combinations_with_sauce(list_ingredients, sauce) -> List[List[Ingredient]]:
    if isinstance(sauce, WithoutSauce):
        list_ingredients.append(sauce)
        return [list_ingredients]

    combinations = []
    for i in range(len(list_ingredients) + 1):
        combination = list_ingredients.copy()
        combination.append(sauce)
        combination[i], combination[-1] = combination[-1], combination[i]
        combinations.append(combination)
    return combinations


def calculate_points(player_level: int, ingredients: List[Ingredient], sauces: List[Sauce]) -> Generator[CalculationResult, None, None]:
    for ingredients_combination in tqdm(itertools.product(ingredients, repeat=3), desc="Calculation dishes", total=175616):
        for sauce in sauces:
            for combination in get_combinations_with_sauce(list(ingredients_combination), sauce):
                r = EpicChefCalculator().calculate(player_level, list(combination))
                yield CalculationResult(
                    ingredients=list(combination),
                    points=r,
                    points_sum=r.vgr+r.sprt+r.soph
                )


if __name__ == "__main__":
    all_ingredients = [i() for i in Ingredient.__subclasses__()]
    all_sauces = [s() for s in Sauce.__subclasses__()]
    cache = []

    try:
        os.remove('epic-chef.db')
    except FileNotFoundError:
        pass

    # Подключаемся к базе данных или создаем ее, если она не существует
    models.Base.metadata.create_all(engine)
    session.commit()

    print("Ok let's go. In and out. 20 minutes adventure.")
    c = 0
    for r in calculate_points(99, all_ingredients, all_sauces):
        levels = []
        tags = set()
        for i in r.ingredients:
            for s in i.synergies:
                levels.append(s.min_level)
            for t in getattr(i, "tags", []):
                tags.add(t.name)
        min_level_required = max(levels) if levels else 0
        session.add(models.Dish(
            vgr=r.points.vgr,
            sprt=r.points.sprt,
            soph=r.points.soph,
            required_level=min_level_required,
            sum_points=r.points_sum,
            ingredient_1_name=r.ingredients[0].name,
            ingredient_1_name_ru=r.ingredients[0].__str__(),
            ingredient_2_name=r.ingredients[1].name,
            ingredient_2_name_ru=r.ingredients[1].__str__(),
            ingredient_3_name=r.ingredients[2].name,
            ingredient_3_name_ru=r.ingredients[2].__str__(),
            ingredient_4_name=r.ingredients[3].name,
            ingredient_4_name_ru=r.ingredients[3].__str__(),
            tags=", ".join(sorted(tags))
        ))
        c += 1
        if c == CACHE_CHUNK_SIZE:
            c = 0
            print("Flush session.")
            session.flush()
            print("Ok it wasn't too hard.")


print("Let's make some indexes. We need it i swear.")
session.execute(text("CREATE INDEX sum_points_index ON dishes('sum_points')"))
session.execute(text("CREATE INDEX required_level_index ON dishes('required_level')"))
session.execute(text("CREATE INDEX ingr1_name_index ON dishes('ingredient_1_name')"))
session.execute(text("CREATE INDEX ingr2_name_index ON dishes('ingredient_2_name')"))
session.execute(text("CREATE INDEX ingr3_name_index ON dishes('ingredient_3_name')"))
session.execute(text("CREATE INDEX ingr4_name_index ON dishes('ingredient_4_name')"))
session.execute(text("CREATE INDEX ingr1_name_ru_index ON dishes('ingredient_1_name_ru')"))
session.execute(text("CREATE INDEX ingr2_name_ru_index ON dishes('ingredient_2_name_ru')"))
session.execute(text("CREATE INDEX ingr3_name_ru_index ON dishes('ingredient_3_name_ru')"))
session.execute(text("CREATE INDEX ingr4_name_ru_index ON dishes('ingredient_4_name_ru')"))

print("We are almost finished. Almost.")

print("The last commit is started. Hope i can do this.")
session.commit()
print("Phew it's all over. May i take a breather now?")
