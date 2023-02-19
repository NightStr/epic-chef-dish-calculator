from typing import List

from dish.base import Sauce, IngredientPoint, BaseExtraBonus


class BasicTomatoSauce(Sauce):
    name = "Basic Tomato Sauce"
    name_ru = "Обычный помидор"
    points = IngredientPoint(vgr=10, sprt=0, soph=0)
    bonuses: List[BaseExtraBonus] = []


class SpectralChutneySauce(Sauce):
    name = "Spectral Chutney Sauce"
    name_ru = "Спектральный соус чатни"
    points = IngredientPoint(vgr=0, sprt=0, soph=20)
    bonuses: List[BaseExtraBonus] = []
