import unittest

from calculations.calculator import EpicChefCalculator
from dish.base import DishPoint
from dish.ingredients import Carrot, Tomato, Potato
from dish.sauces import BasicTomatoSauce


class MyClassTest(unittest.TestCase):
    def test_carrot_tomato_potato_with_basic_tomato_sauce(self):
        self.assertEqual(EpicChefCalculator().calculate([
            Carrot(), Tomato(), Potato(), BasicTomatoSauce()
        ]), DishPoint(
            vgr=25,
            sprt=15,
            soph=15
        ))
