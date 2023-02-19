from typing import List

from dish.base import Ingredient, IngredientPoint, BasePoint, BaseBonusMechanic, BaseBonusCondition, BaseExtraBonus
from dish.bonus_conditions import PreviousIngredientsHaveAllTags, HaveNoPreviousIngredients, HaveIngredientInIngredients
from dish.bonus_mechanics import FlatBonusMechanic
from dish.bonuses import AllConditionsExtraBonus
from dish.tags import Tag


class Tomato(Ingredient):
    tags: List[Tag] = [Tag.land, Tag.plant]
    points = IngredientPoint(
        vgr=6,
        sprt=2,
        soph=2,
    )
    bonuses: List[BaseExtraBonus] = [
        AllConditionsExtraBonus(
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.plant, Tag.land])],
            mechanics=[FlatBonusMechanic(bonuses=BasePoint(vgr=5, sprt=0, soph=0))]
        )
    ]


class Carrot(Ingredient):
    tags: List[Tag] = [Tag.land, Tag.plant]
    points = IngredientPoint(
        vgr=2,
        sprt=5,
        soph=3,
    )
    bonuses: List[BaseExtraBonus] = [
        AllConditionsExtraBonus(
            conditions=[HaveNoPreviousIngredients()],
            mechanics=[FlatBonusMechanic(bonuses=BasePoint(
                vgr=0,
                sprt=5,
                soph=0
            ))]
        )
    ]


class Potato(Ingredient):
    tags: List[Tag] = [Tag.land, Tag.plant]
    points = IngredientPoint(
        vgr=2,
        sprt=3,
        soph=5,
    )
    bonuses: List[BaseExtraBonus] = [
        AllConditionsExtraBonus(
            conditions=[HaveIngredientInIngredients(ingredient=Tomato)],
            mechanics=[FlatBonusMechanic(bonuses=BasePoint(
                vgr=0,
                sprt=0,
                soph=5
            ))]
        )
    ]
