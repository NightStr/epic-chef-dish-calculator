from typing import List

from dish.base import Sauce, IngredientPoint, BaseSynergy


class BasicTomatoSauce(Sauce):
    name = "Basic Tomato Sauce"
    name_ru = "Обычный помидор"
    points = IngredientPoint(vgr=10, sprt=0, soph=0)
    synergies: List[BaseSynergy] = []


class RiceBechamelSauce(Sauce):
    name = "Rice Bechamel Sauce"
    name_ru = "Рисовый соус бешамель"
    points = IngredientPoint(vgr=0, sprt=10, soph=0)
    synergies: List[BaseSynergy] = []


class MushroomSauce(Sauce):
    name = "Mushroom Sauce"
    name_ru = "Грибной соус"
    points = IngredientPoint(vgr=0, sprt=0, soph=10)
    synergies: List[BaseSynergy] = []


class SpectralChutneySauce(Sauce):
    name = "Spectral Chutney Sauce"
    name_ru = "Спектральный соус чатни"
    points = IngredientPoint(vgr=0, sprt=0, soph=20)
    synergies: List[BaseSynergy] = []


class MarconnaiseSauce(Sauce):
    name = "Marconnaise Sauce"
    name_ru = "Соус «Марконнез»"
    points = IngredientPoint(vgr=20, sprt=0, soph=0)
    synergies: List[BaseSynergy] = []


class SpecialCreamSauce(Sauce):
    name = "Special Cream Sauce"
    name_ru = "Особый сливочный соус"
    points = IngredientPoint(vgr=0, sprt=20, soph=0)
    synergies: List[BaseSynergy] = []


class SpiritPotatoSauce(Sauce):
    name = "Spirit Potato Sauce"
    name_ru = "Душевный картофельный соус"
    points = IngredientPoint(vgr=50, sprt=0, soph=0)
    synergies: List[BaseSynergy] = []


class ShellFondueSauce(Sauce):
    name = "Shell Fondue Sauce"
    name_ru = "Shell Fondue Sauce"
    points = IngredientPoint(vgr=0, sprt=50, soph=0)
    synergies: List[BaseSynergy] = []


class DarkSeafoodSauce(Sauce):
    name = "Dark Seafood Sauce"
    name_ru = "Тёмный соус из морепродуктов"
    points = IngredientPoint(vgr=0, sprt=0, soph=50)
    synergies: List[BaseSynergy] = []


class WithoutSauce(Sauce):
    name = "Without sauce"
    name_ru = "Без соуса"
    points = IngredientPoint(vgr=0, sprt=0, soph=0)
    synergies: List[BaseSynergy] = []
