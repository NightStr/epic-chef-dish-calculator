from typing import List

from calculations.base import BaseCalculator
from dish.base import BaseIngredient, Sauce
from dish.points import DishPoint


class EpicChefCalculator(BaseCalculator):
    def calculate(self, ingredients: List[BaseIngredient]) -> DishPoint:
        dish_points = DishPoint(0, 0, 0)
        print(f"Начинаем готовку из ингридиентов: {ingredients}")
        ingredients_before = []
        for i in ingredients:
            dish_points = i.apply(
                dish_points,
                ingredients=[i for i in ingredients_before if not issubclass(i, Sauce)]
            )
            ingredients_before.append(i)
        print(f"Блюдо готово. Ингридиенты: {ingredients}. Результат: {dish_points}")
