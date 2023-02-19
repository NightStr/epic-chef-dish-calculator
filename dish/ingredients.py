from typing import List

from dish.base import Ingredient, IngredientPoint, BasePoint, BaseBonusMechanic, BaseBonusCondition, BaseExtraBonus
from dish.bonus_conditions import PreviousIngredientsHaveAllTags, HaveNoPreviousIngredients, HaveIngredientInIngredients
from dish.bonus_mechanics import FlatBonusMechanic
from dish.bonuses import AllConditionsExtraBonus
from dish.tags import Tag


class Tomato(Ingredient):
    name = "Tomato"
    name_ru = "Помидор"
    tags: List[Tag] = [Tag.land, Tag.plant]
    points = IngredientPoint(
        vgr=6,
        sprt=2,
        soph=2,
    )
    bonuses: List[BaseExtraBonus] = [
        AllConditionsExtraBonus(
            min_level=2,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.plant, Tag.land])],
            mechanics=[FlatBonusMechanic(bonuses=BasePoint(vgr=5, sprt=0, soph=0))]
        )
    ]


class Carrot(Ingredient):
    name = "Carrot"
    name_ru = "Морковь"
    tags: List[Tag] = [Tag.land, Tag.plant]
    points = IngredientPoint(
        vgr=2,
        sprt=5,
        soph=3,
    )
    bonuses: List[BaseExtraBonus] = [
        AllConditionsExtraBonus(
            min_level=2,
            conditions=[HaveNoPreviousIngredients()],
            mechanics=[FlatBonusMechanic(bonuses=BasePoint(
                vgr=0,
                sprt=5,
                soph=0
            ))]
        )
    ]


class Potato(Ingredient):
    name = "Potato"
    name_ru = "Картофель"
    tags: List[Tag] = [Tag.land, Tag.plant]
    points = IngredientPoint(
        vgr=2,
        sprt=3,
        soph=5,
    )
    bonuses: List[BaseExtraBonus] = [
        AllConditionsExtraBonus(
            min_level=2,
            conditions=[HaveIngredientInIngredients(ingredient="Tomato")],
            mechanics=[FlatBonusMechanic(bonuses=BasePoint(
                vgr=0,
                sprt=0,
                soph=5
            ))]
        )
    ]
