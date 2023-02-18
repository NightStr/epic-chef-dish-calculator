import abc
from abc import ABC
from dataclasses import dataclass
from typing import List, Tuple

from pydantic import BaseModel

from dish.tags import Tag


class BaseIngredient(BaseModel):
    points: "IngredientPoint"

    def _apply(self, dish_points: "DishPoint", ingredients: List["Ingredient"]) -> "DishPoint":
        return dish_points

    def apply(self, dish_points: "DishPoint", ingredients: List["Ingredient"]) -> "DishPoint":
        return self._apply(dish_points.copy(), ingredients).add_ingredient(self)


class BasePoint(BaseModel):
    vgr: int
    sprt: int
    soph: int


class IngredientPoint(BasePoint):
    ...


class DishPoint(BasePoint):
    def copy(self) -> "DishPoint":
        return DishPoint(
            vgr=self.vgr,
            sprt=self.sprt,
            soph=self.soph
        )

    def add_ingredient(self, ingredient: BaseIngredient) -> "DishPoint":
        return DishPoint(
            vgr=self.vgr + ingredient.points.vgr,
            sprt=self.sprt + ingredient.points.sprt,
            soph=self.soph + ingredient.points.soph
        )


class Sauce(BaseIngredient):
    def _apply(self, dish_points: DishPoint, ingredients: List["Ingredient"]) -> DishPoint:
        return dish_points


class Ingredient(BaseIngredient, ABC):
    tags: List[Tag]
