from typing import List

from dish.base import Ingredient, IngredientPoint, DishPoint
from dish.tags import Tag


class Tomato(Ingredient):
    tags: List[Tag] = [Tag.land, Tag.plant]
    points = IngredientPoint(
        vgr=6,
        sprt=2,
        soph=2,
    )

    def _apply(self, dish_points: DishPoint, ingredients: List[Ingredient]) -> DishPoint:
        exists_tags = []

        for i in ingredients:
            exists_tags.extend(i.tags)

        if Tag.plant in exists_tags and Tag.land in exists_tags:
            dish_points.vgr = dish_points.vgr + 5

        return dish_points


class Carrot(Ingredient):
    tags: List[Tag] = [Tag.land, Tag.plant]
    points = IngredientPoint(
        vgr=2,
        sprt=5,
        soph=3,
    )

    def _apply(self, dish_points: DishPoint, ingredients: List[Ingredient]) -> DishPoint:
        if not ingredients:
            dish_points.sprt = dish_points.sprt + 5

        return dish_points


class Potato(Ingredient):
    tags: List[Tag] = [Tag.land, Tag.plant]
    points = IngredientPoint(
        vgr=2,
        sprt=3,
        soph=5,
    )

    def _apply(self, dish_points: DishPoint, ingredients: List[Ingredient]) -> DishPoint:
        if Tomato in [i.__class__ for i in ingredients]:
            dish_points.soph = dish_points.soph + 5

        return dish_points
