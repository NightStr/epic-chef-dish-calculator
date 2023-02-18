from dish.base import Sauce
from dish.points import IngredientPoint


class BasicTomatoSauce(Sauce):
    points = IngredientPoint(vgr=10, sprt=0, soph=0)
