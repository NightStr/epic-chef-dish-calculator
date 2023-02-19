import unittest

from calculations.calculator import EpicChefCalculator
from dish.base import DishPoint
from dish.ingredients import *
from dish.sauces import *


class MyClassTest(unittest.TestCase):
    def test_carrot_tomato_potato_with_basic_tomato_sauce(self):
        self.assertEqual(EpicChefCalculator().calculate(99, [
            Carrot(), Tomato(), Potato(), BasicTomatoSauce()
        ]), DishPoint(
            vgr=25,
            sprt=15,
            soph=15
        ))

    def test_ghostato_hypnofish_specialdough_with_spectral_chutney_sauce(self):
        self.assertEqual(EpicChefCalculator().calculate(30, [
            Ghostato(), Hypnofish(), SpectralChutneySauce(), SpecialDough(),
        ]), DishPoint(
            vgr=15,
            sprt=23,
            soph=192.6
        ))

    def test_spiderflesh_legendarycrab_legendarycrab_with_spectral_chutney_sauce(self):
        self.assertEqual(EpicChefCalculator().calculate(60, [
            SpiderFlesh(), SpectralChutneySauce(), LegendaryCrab(), LegendaryCrab(),
        ]), DishPoint(
            vgr=67,
            sprt=56,
            soph=526.75
        ))
