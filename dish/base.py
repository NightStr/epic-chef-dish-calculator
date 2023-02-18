import abc
from abc import ABC
from dataclasses import dataclass
from typing import List, Tuple

from dish.points import IngredientPoint, DishPoint
from dish.tags import Tag


@dataclass
class BaseIngredient(abc.ABC):
    points: IngredientPoint

    @abc.abstractmethod
    def _apply(self, dish_points: DishPoint, ingredients: List["Ingredient"]) -> DishPoint: ...

    def apply(self, dish_points: DishPoint, ingredients: List["Ingredient"]) -> DishPoint:
        return self._apply(dish_points.copy(), ingredients).add_ingredient(self)


class Sauce(BaseIngredient, ABC):
    ...


@dataclass
class Ingredient(BaseIngredient, ABC):
    tags: Tuple[Tag, Tag]
