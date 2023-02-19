import abc
from abc import ABC
from typing import List

from pydantic import BaseModel

from dish.tags import Tag




class BaseBonusCondition(BaseModel):
    def can_apply(self, ingredients: List["Ingredient"]) -> bool:
        return False


class BaseBonusMechanic(BaseModel):
    @abc.abstractmethod
    def apply(self, dish_points: "DishPoint") -> "DishPoint":
        return dish_points


class BaseIngredient(BaseModel):
    name: str
    name_ru: str
    points: "IngredientPoint"
    bonuses: List["BaseExtraBonus"]

    def __str__(self):
        return f"{self.name} ({self.name_ru})"

    def apply(self, player_level: int, dish_points: "DishPoint", ingredients: List["Ingredient"]) -> "DishPoint":
        for bonus in self.bonuses:
            dish_points = bonus.apply(player_level, dish_points, ingredients)
        return dish_points + self.points


class BasePoint(BaseModel):
    vgr: float
    sprt: float
    soph: float

    def __add__(self, other):
        return self.__class__(
            vgr=self.vgr + other.vgr,
            sprt=self.sprt + other.sprt,
            soph=self.soph + other.soph,
        )

    def __mul__(self, other):
        return self.__class__(
            vgr=self.vgr * other.vgr,
            sprt=self.sprt * other.sprt,
            soph=self.soph * other.soph,
        )


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
    ...


class Ingredient(BaseIngredient, ABC):
    tags: List[Tag]


class BaseExtraBonus(BaseModel):
    min_level: int
    conditions: List[BaseBonusCondition]
    mechanics: List[BaseBonusMechanic]

    def can_apply(self, player_levent: int, ingredients: List[Ingredient]) -> bool:
        return player_levent >= self.min_level

    def apply(self, player_levent: int, dish_points: DishPoint, ingredients: List[Ingredient]) -> DishPoint:
        dish_points_c = dish_points.copy()
        if self.can_apply(player_levent, ingredients):
            for m in self.mechanics:
                dish_points_c = m.apply(dish_points_c)
        return dish_points_c
