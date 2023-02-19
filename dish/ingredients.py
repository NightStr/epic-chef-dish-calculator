from typing import List

from dish.base import Ingredient, IngredientPoint, BasePoint, BaseBonusMechanic, BaseBonusCondition, BaseExtraBonus
from dish.bonus_conditions import PreviousIngredientsHaveAllTags, HaveNoPreviousIngredients, HaveIngredientInIngredients
from dish.bonus_mechanics import FlatBonusMechanic, MultiplierBonusMechanic
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


class Rice(Ingredient):
    name = "Rice"
    name_ru = "Рис"
    tags: List[Tag] = [Tag.land, Tag.plant]
    points = IngredientPoint(
        vgr=1,
        sprt=3,
        soph=6,
    )
    bonuses: List[BaseExtraBonus] = [
        AllConditionsExtraBonus(
            min_level=2,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.plant, Tag.mixed])],
            mechanics=[FlatBonusMechanic(bonuses=BasePoint(vgr=0, sprt=5, soph=0))]
        )
    ]


class Hypnofish(Ingredient):
    name = "Hypnofish"
    name_ru = "Гипнорыба"
    tags: List[Tag] = [Tag.sea, Tag.animal]
    points = IngredientPoint(
        vgr=11,
        sprt=7,
        soph=17,
    )
    bonuses: List[BaseExtraBonus] = [
        AllConditionsExtraBonus(
            min_level=19,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.plant, Tag.sea])],
            mechanics=[FlatBonusMechanic(bonuses=BasePoint(vgr=30, sprt=0, soph=0))]
        )
    ]


class Ghostato(Ingredient):
    name = "Ghostato"
    name_ru = "Спектрофель"
    tags: List[Tag] = [Tag.mixed, Tag.magic]
    points = IngredientPoint(
        vgr=0,
        sprt=8,
        soph=12,
    )
    bonuses: List[BaseExtraBonus] = [
        AllConditionsExtraBonus(
            min_level=2,
            conditions=[HaveIngredientInIngredients(ingredient="Rice")],
            mechanics=[FlatBonusMechanic(bonuses=BasePoint(
                vgr=0,
                sprt=0,
                soph=15
            ))]
        ),
        AllConditionsExtraBonus(
            min_level=10,
            conditions=[HaveNoPreviousIngredients()],
            mechanics=[FlatBonusMechanic(bonuses=BasePoint(
                vgr=0,
                sprt=0,
                soph=30
            ))]
        )
    ]


class SpecialDough(Ingredient):
    name = "Special Dough"
    name_ru = "Особое тесто"
    tags: List[Tag] = [Tag.mixed, Tag.plant]
    points = IngredientPoint(
        vgr=4,
        sprt=8,
        soph=3,
    )
    bonuses: List[BaseExtraBonus] = [
        AllConditionsExtraBonus(
            min_level=16,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.magic, Tag.sea])],
            mechanics=[MultiplierBonusMechanic(bonuses=BasePoint(
                vgr=0,
                sprt=0,
                soph=2.4
            ))]
        ),
        AllConditionsExtraBonus(
            min_level=2,
            conditions=[HaveNoPreviousIngredients()],
            mechanics=[FlatBonusMechanic(bonuses=BasePoint(
                vgr=7,
                sprt=0,
                soph=0
            ))]
        )
    ]