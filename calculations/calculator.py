from typing import List

from calculations.base import BaseCalculator
from dish.base import BaseIngredient, Sauce, DishPoint


class EpicChefCalculator(BaseCalculator):
    def calculate(self, player_level: int, ingredients: List[BaseIngredient]) -> DishPoint:
        dish_points = DishPoint(vgr=0, sprt=0, soph=0)
        print(f"Начинаем готовку из ингридиентов: {ingredients}")
        ingredients_before = []
        for i in ingredients:
            dish_points = i.apply(
                player_level,
                dish_points,
                ingredients=[i for i in ingredients_before if not issubclass(i.__class__, Sauce)]
            )
            ingredients_before.append(i)
        print(f"Блюдо готово. Ингридиенты: {ingredients}. Результат: {dish_points}")
        return dish_points
