from typing import List

from dish.base import Sauce, IngredientPoint, BaseExtraBonus


class BasicTomatoSauce(Sauce):
    points = IngredientPoint(vgr=10, sprt=0, soph=0)
    bonuses: List[BaseExtraBonus] = []
