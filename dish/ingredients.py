from typing import List

from dish.base import Ingredient, IngredientPoint, BasePoint, BaseSynergyMechanic, BaseSynergyCondition, BaseSynergy
from dish.bonus_conditions import PreviousIngredientsHaveAllTags, MustBeFirstIngredient, SpecificIngredientRequired
from dish.bonus_mechanics import FlatSynergyMechanic, MultiplierSynergyMechanic
from dish.bonuses import AllConditionsSynergy
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
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=2,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.plant, Tag.land])],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=5, sprt=0, soph=0))]
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
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=2,
            conditions=[MustBeFirstIngredient()],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(
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
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=2,
            conditions=[SpecificIngredientRequired(ingredient="Tomato")],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(
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
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=2,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.plant, Tag.mixed])],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=5, soph=0))]
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
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=19,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.plant, Tag.sea])],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=30, sprt=0, soph=0))]
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
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=2,
            conditions=[SpecificIngredientRequired(ingredient="Rice")],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(
                vgr=0,
                sprt=0,
                soph=15
            ))]
        ),
        AllConditionsSynergy(
            min_level=10,
            conditions=[MustBeFirstIngredient()],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(
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
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=16,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.magic, Tag.sea])],
            mechanics=[MultiplierSynergyMechanic(bonuses=BasePoint(
                vgr=0,
                sprt=0,
                soph=2.4
            ))]
        ),
        AllConditionsSynergy(
            min_level=2,
            conditions=[MustBeFirstIngredient()],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(
                vgr=7,
                sprt=0,
                soph=0
            ))]
        )
    ]


class SpiderFlesh(Ingredient):
    name = "Spider Flesh"
    name_ru = "Паучье мясо"
    tags: List[Tag] = [Tag.land, Tag.magic]
    points = IngredientPoint(
        vgr=15,
        sprt=23,
        soph=12,
    )
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=40,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.animal, Tag.sea])],
            mechanics=[
                FlatSynergyMechanic(bonuses=BasePoint(
                    vgr=15,
                    sprt=0,
                    soph=0
                )),
                MultiplierSynergyMechanic(bonuses=BasePoint(
                    vgr=2,
                    sprt=0,
                    soph=0
                ))
            ]
        ),
        AllConditionsSynergy(
            min_level=2,
            conditions=[MustBeFirstIngredient()],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(
                vgr=12,
                sprt=9,
                soph=10
            ))]
        )
    ]


class LegendaryCrab(Ingredient):
    name = "Legendary Crab"
    name_ru = "Легендарный краб"
    tags: List[Tag] = [Tag.sea, Tag.animal]
    points = IngredientPoint(
        vgr=20,
        sprt=12,
        soph=13,
    )
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=47,
            conditions=[SpecificIngredientRequired(ingredient="Mugle Carp")],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(
                vgr=40,
                sprt=0,
                soph=0
            ))]
        ),
        AllConditionsSynergy(
            min_level=2,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.land, Tag.magic])],
            mechanics=[
                FlatSynergyMechanic(bonuses=BasePoint(
                    vgr=0,
                    sprt=0,
                    soph=25
                )),
                MultiplierSynergyMechanic(bonuses=BasePoint(
                    vgr=0,
                    sprt=0,
                    soph=2.5
                ))
            ]
        )
    ]


class MugleCarp(Ingredient):
    name = "Mugle Carp"
    name_ru = "Магл-карп"
    tags: List[Tag] = [Tag.sea, Tag.animal]
    points = IngredientPoint(
        vgr=8,
        sprt=12,
        soph=20,
    )
    synergies: List[BaseSynergy] = []
