import abc
from typing import List

from dish.base import BaseIngredient
from dish.points import DishPoint


class BaseCalculator(abc.ABC):
    @abc.abstractmethod
    def calculate(self, ingredients: List[BaseIngredient]) -> DishPoint:
        ...
