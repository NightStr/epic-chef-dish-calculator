import abc
from typing import List

from dish.base import BaseIngredient, DishPoint


class BaseCalculator(abc.ABC):
    @abc.abstractmethod
    def calculate(self, player_level: int, ingredients: List[BaseIngredient]) -> DishPoint:
        ...
