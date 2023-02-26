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


def calculate_points(player_level: int, ingredients: List[Ingredient], sauces: List[Sauce]) -> Generator[CalculationResult, None, None]:
    for ingredients_combination in tqdm(itertools.product(ingredients, repeat=3), desc="Calculation dishes", total=175616):
        for sauce in sauces:
            list_ingredients = list(ingredients_combination)
            combinations = []
            for i in range(len(list_ingredients)+1):
                combination = list_ingredients.copy()
                combination.append(sauce)
                combination[i], combination[-1] = combination[-1], combination[i]
                combinations.append(combination)
            for combination in combinations:
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
    for ingredient in itertools.chain(all_ingredients, all_sauces):
        tags = []
        for tag in getattr(ingredient, "tags", []):
            tag_model = session.query(models.Tag).filter_by(name=tag.name).first()
            if not tag_model:
                tag_model = models.Tag(name=tag.name)
                session.add(tag_model)
                session.flush()
            tags.append(tag_model)
        session.flush()
        ingredient = models.Ingredient(
            name=ingredient.name,
            name_ru=ingredient.name_ru,
            vgr=ingredient.points.vgr,
            sprt=ingredient.points.sprt,
            soph=ingredient.points.soph,
        )
        session.add(ingredient)
        for tag in tags:
            session.add(models.IngredientTag(
                ingredient_id=ingredient.name,
                tag_id=tag.id
            ))
    c = 0
    for r in calculate_points(99, all_ingredients, all_sauces):
        levels = []
        for i in r.ingredients:
            for s in i.synergies:
                levels.append(s.min_level)
        min_level_required = max(levels) if levels else 0
        dish = models.Dish(
            vgr=r.points.vgr,
            sprt=r.points.sprt,
            soph=r.points.soph,
            required_level=min_level_required,
            sum_points=r.points_sum
        )
        session.add(dish)
        cache.append({
            "dish": dish,
            "ingredients": {index: ing for index, ing in enumerate(r.ingredients)}
        })
        c += 1
        if c == CACHE_CHUNK_SIZE:
            c = 0
            print("Flush dishes.")
            session.flush()
            print("Ok it wasn't too hard.")
            for v in tqdm(cache, desc="dumping cache into db", total=CACHE_CHUNK_SIZE):
                try:
                    for index, ing in v["ingredients"].items():
                        session.add(models.DishIngredient(
                            dish_id=v["dish"].id,
                            ingredient_id=ing.name,
                            ord=index
                        ))
                except TypeError:
                    raise
            cache = []
            print("Flush DishIngredient")
            session.flush()
            print("Ok, ok, let's continue. Fuuuu, i so tired, can i just die?")

print("Let's make some indexes. We need it i swear.")
session.execute(text("CREATE INDEX sum_points_index ON dishes('sum_points')"))
session.execute(text("CREATE INDEX required_level_index ON dishes('required_level')"))
print("We are almost finished. Almost.")

print("The last commit is started. Hope i can do this.")
session.commit()
print("Phew it's all over. May i take a breather now?")
