from typing import List

from dish.base import Ingredient, IngredientPoint, BasePoint, BaseSynergy
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
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=5, soph=0))]
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
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=0, soph=5))]
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
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=0, soph=15))]
        ),
        AllConditionsSynergy(
            min_level=10,
            conditions=[MustBeFirstIngredient()],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=0, soph=30))]
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
            mechanics=[MultiplierSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=0, soph=2.4))]
        ),
        AllConditionsSynergy(
            min_level=2,
            conditions=[MustBeFirstIngredient()],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=7, sprt=0, soph=0))]
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
                FlatSynergyMechanic(bonuses=BasePoint(vgr=15, sprt=0, soph=0)),
                MultiplierSynergyMechanic(bonuses=BasePoint(vgr=2, sprt=0, soph=0))
            ]
        ),
        AllConditionsSynergy(
            min_level=2,
            conditions=[MustBeFirstIngredient()],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=12, sprt=9, soph=10))]
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
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=40, sprt=0, soph=0))]
        ),
        AllConditionsSynergy(
            min_level=2,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.land, Tag.magic])],
            mechanics=[
                FlatSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=0, soph=25)),
                MultiplierSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=0, soph=2.5))
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


class Mushroom(Ingredient):
    name = "Mushroom"
    name_ru = "Гриб"
    tags: List[Tag] = [Tag.land, Tag.plant]
    points = IngredientPoint(
        vgr=1,
        sprt=1,
        soph=3,
    )
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=2,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.sea])],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=10, soph=0))]
        )
    ]


class Apple(Ingredient):
    name = "Apple"
    name_ru = "Яблоко"
    tags: List[Tag] = [Tag.land, Tag.plant]
    points = IngredientPoint(
        vgr=6,
        sprt=4,
        soph=5,
    )
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=5,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.mixed, Tag.animal])],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=9, sprt=0, soph=0))]
        )
    ]


class Wood(Ingredient):
    name = "Wood"
    name_ru = "Дерево"
    tags: List[Tag] = [Tag.land, Tag.plant]
    points = IngredientPoint(
        vgr=1,
        sprt=1,
        soph=1,
    )
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=2,
            conditions=[SpecificIngredientRequired(ingredient="Apple Wood")],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=5, soph=0))]
        )
    ]


class AppleWood(Ingredient):
    name = "Apple Wood"
    name_ru = "Яблочная древесина"
    tags: List[Tag] = [Tag.land, Tag.plant]
    points = IngredientPoint(
        vgr=2,
        sprt=2,
        soph=2,
    )
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=6,
            conditions=[SpecificIngredientRequired(ingredient="Erwin Wood")],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=8, soph=0))]
        )
    ]


class ErwinWood(Ingredient):
    name = "Erwin Wood"
    name_ru = "Эрвиново дерево"
    tags: List[Tag] = [Tag.land, Tag.plant]
    points = IngredientPoint(
        vgr=3,
        sprt=3,
        soph=3,
    )
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=27,
            conditions=[MustBeFirstIngredient()],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=27, soph=0))]
        )
    ]


class SeagullEgg(Ingredient):
    name = "Seagull Egg"
    name_ru = "Яйцо чайки"
    tags: List[Tag] = [Tag.land, Tag.animal]
    points = IngredientPoint(
        vgr=3,
        sprt=2,
        soph=0,
    )
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=3,
            conditions=[SpecificIngredientRequired(ingredient="Potato")],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=7, soph=0))]
        ),
        AllConditionsSynergy(
            min_level=22,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.mixed, Tag.magic])],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=40, soph=0))]
        )
    ]


class Rat(Ingredient):
    name = "Rat"
    name_ru = "Крыса"
    tags: List[Tag] = [Tag.land, Tag.animal]
    points = IngredientPoint(
        vgr=4,
        sprt=1,
        soph=0,
    )
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=2,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.land, Tag.plant])],
            mechanics=[MultiplierSynergyMechanic(bonuses=BasePoint(vgr=1.5, sprt=0, soph=0))]
        )
    ]


class Milk(Ingredient):
    name = "Milk"
    name_ru = "Молоко"
    tags: List[Tag] = [Tag.land, Tag.animal]
    points = IngredientPoint(
        vgr=5,
        sprt=3,
        soph=7,
    )
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=7,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.land, Tag.plant])],
            mechanics=[MultiplierSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=0, soph=1.6))]
        )
    ]


class CowMeat(Ingredient):
    name = "Cow Meat"
    name_ru = "Говядина"
    tags: List[Tag] = [Tag.land, Tag.animal]
    points = IngredientPoint(
        vgr=11,
        sprt=6,
        soph=3,
    )
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=12,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.plant, Tag.land])],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=18, soph=0))]
        )
    ]


class PangunEgg(Ingredient):
    name = "Pangun Egg"
    name_ru = "Яйцо пангуна"
    tags: List[Tag] = [Tag.land, Tag.animal]
    points = IngredientPoint(
        vgr=9,
        sprt=7,
        soph=14,
    )
    synergies: List[BaseSynergy] = []


class PangunMeat(Ingredient):
    name = "Pangun Meat"
    name_ru = "Мясо пангуна"
    tags: List[Tag] = [Tag.land, Tag.animal]
    points = IngredientPoint(
        vgr=14,
        sprt=12,
        soph=4,
    )
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=24,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.magic, Tag.mixed])],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=25, soph=0))]
        ),
        AllConditionsSynergy(
            min_level=19,
            conditions=[MustBeFirstIngredient()],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=7, sprt=0, soph=0))]
        )
    ]


class GomeraShell(Ingredient):
    name = "Gomera Shell"
    name_ru = "Панцирь гомеры"
    tags: List[Tag] = [Tag.land, Tag.animal]
    points = IngredientPoint(
        vgr=14,
        sprt=16,
        soph=15,
    )
    synergies: List[BaseSynergy] = []


class GomeraMeat(Ingredient):
    name = "Gomera Meat"
    name_ru = "Мясо гомеры"
    tags: List[Tag] = [Tag.land, Tag.animal]
    points = IngredientPoint(
        vgr=7,
        sprt=27,
        soph=16,
    )
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=46,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.animal, Tag.mixed])],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=0, soph=35))]
        ),
        AllConditionsSynergy(
            min_level=2,
            conditions=[MustBeFirstIngredient()],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=30, sprt=0, soph=25))]
        )
    ]


class EvilMandragora(Ingredient):
    name = "Evil Mandragora"
    name_ru = "Злая мандрагора"
    tags: List[Tag] = [Tag.land, Tag.magic]
    points = IngredientPoint(
        vgr=9,
        sprt=8,
        soph=3,
    )
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=9,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.sea, Tag.animal])],
            mechanics=[MultiplierSynergyMechanic(bonuses=BasePoint(vgr=1.8, sprt=0, soph=0))]
        )
    ]


class Erwin(Ingredient):
    name = "Erwin"
    name_ru = "Эрвинов плод"
    tags: List[Tag] = [Tag.land, Tag.magic]
    points = IngredientPoint(
        vgr=6,
        sprt=9,
        soph=5,
    )
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=19,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.mixed, Tag.animal])],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=20, sprt=0, soph=0))]
        )
    ]


class UnicornDelight(Ingredient):
    name = "Unicorn Delight"
    name_ru = "Единорожьи яблоки"
    tags: List[Tag] = [Tag.land, Tag.magic]
    points = IngredientPoint(
        vgr=10,
        sprt=16,
        soph=9,
    )
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=39,
            conditions=[SpecificIngredientRequired(ingredient="Mugle Carp")],
            mechanics=[MultiplierSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=0, soph=3))]
        ),
        AllConditionsSynergy(
            min_level=2,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.mixed, Tag.animal])],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=27, soph=0))]
        )
    ]


class UnicornBacon(Ingredient):
    name = "Unicorn Bacon"
    name_ru = "Единорожий бекон"
    tags: List[Tag] = [Tag.land, Tag.magic]
    points = IngredientPoint(
        vgr=12,
        sprt=6,
        soph=17,
    )
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=2,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.land, Tag.plant])],
            mechanics=[MultiplierSynergyMechanic(bonuses=BasePoint(vgr=2.2, sprt=0, soph=0))]
        ),
        AllConditionsSynergy(
            min_level=26,
            conditions=[MustBeFirstIngredient()],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=18, soph=0))]
        )
    ]


class SpiderSilk(Ingredient):
    name = "Spider Silk"
    name_ru = "Паучья нить"
    tags: List[Tag] = [Tag.land, Tag.magic]
    points = IngredientPoint(
        vgr=14,
        sprt=11,
        soph=20,
    )
    synergies: List[BaseSynergy] = []


class DragonEgg(Ingredient):
    name = "Dragon Egg"
    name_ru = "Яйцо дракона"
    tags: List[Tag] = [Tag.land, Tag.magic]
    points = IngredientPoint(
        vgr=34,
        sprt=25,
        soph=21,
    )
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=50,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.sea, Tag.magic])],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=80, sprt=0, soph=60))]
        ),
        AllConditionsSynergy(
            min_level=2,
            conditions=[MustBeFirstIngredient()],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=40, sprt=40, soph=0))]
        ),
        AllConditionsSynergy(
            min_level=60,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.sea, Tag.animal])],
            mechanics=[MultiplierSynergyMechanic(bonuses=BasePoint(vgr=4, sprt=0, soph=3.6))]
        )
    ]


class Seaweed(Ingredient):
    name = "Seaweed"
    name_ru = "Водоросли"
    tags: List[Tag] = [Tag.sea, Tag.plant]
    points = IngredientPoint(
        vgr=1,
        sprt=3,
        soph=1,
    )
    synergies: List[BaseSynergy] = []


class Crab(Ingredient):
    name = "Crab"
    name_ru = "Краб"
    tags: List[Tag] = [Tag.sea, Tag.animal]
    points = IngredientPoint(
        vgr=2,
        sprt=2,
        soph=1,
    )
    synergies: List[BaseSynergy] = []


class MudEel(Ingredient):
    name = "Mud Eel"
    name_ru = "Илистый угорь"
    tags: List[Tag] = [Tag.sea, Tag.animal]
    points = IngredientPoint(
        vgr=2,
        sprt=10,
        soph=13,
    )
    synergies: List[BaseSynergy] = []


class Biclopus(Ingredient):
    name = "Biclopus"
    name_ru = "Биклоп"
    tags: List[Tag] = [Tag.sea, Tag.animal]
    points = IngredientPoint(
        vgr=6,
        sprt=6,
        soph=13,
    )
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=14,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.land, Tag.magic])],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=10, sprt=10, soph=0))]
        )
    ]


class CucumberSquid(Ingredient):
    name = "Cucumber Squid"
    name_ru = "Огуречный кальмар"
    tags: List[Tag] = [Tag.sea, Tag.animal]
    points = IngredientPoint(
        vgr=9,
        sprt=8,
        soph=8,
    )
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=2,
            conditions=[MustBeFirstIngredient()],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=0, soph=20))]
        )
    ]


class DepthsCrab(Ingredient):
    name = "Depths Crab"
    name_ru = "Глубинный краб"
    tags: List[Tag] = [Tag.sea, Tag.animal]
    points = IngredientPoint(
        vgr=19,
        sprt=13,
        soph=3,
    )
    synergies: List[BaseSynergy] = []


class SandBlowfish(Ingredient):
    name = "Sand Blowfish"
    name_ru = "Песчаная рыба-ёж"
    tags: List[Tag] = [Tag.sea, Tag.animal]
    points = IngredientPoint(
        vgr=3,
        sprt=19,
        soph=13,
    )
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=2,
            conditions=[MustBeFirstIngredient()],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=0, soph=30))]
        )
    ]


class StrawberryJellyfish(Ingredient):
    name = "Strawberry Jellyfish"
    name_ru = "Клубничная медуза"
    tags: List[Tag] = [Tag.sea, Tag.animal]
    points = IngredientPoint(
        vgr=20,
        sprt=11,
        soph=9,
    )
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=2,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.mixed, Tag.magic])],
            mechanics=[MultiplierSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=2.4, soph=0))]
        ),
        AllConditionsSynergy(
            min_level=43,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.land, Tag.magic])],
            mechanics=[
                FlatSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=0, soph=20)),
                MultiplierSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=0, soph=2))
            ]
        )
    ]


class RoyalEel(Ingredient):
    name = "Royal Eel"
    name_ru = "Королевский угорь"
    tags: List[Tag] = [Tag.sea, Tag.animal]
    points = IngredientPoint(
        vgr=2,
        sprt=20,
        soph=23,
    )
    synergies: List[BaseSynergy] = []


class EpicBlowfish(Ingredient):
    name = "Epic Blowfish"
    name_ru = "Былинная рыба-ёж"
    tags: List[Tag] = [Tag.sea, Tag.animal]
    points = IngredientPoint(
        vgr=24,
        sprt=4,
        soph=12,
    )
    synergies: List[BaseSynergy] = []


class QueenCarp(Ingredient):
    name = "Queen Carp"
    name_ru = "Королева-карп"
    tags: List[Tag] = [Tag.sea, Tag.animal]
    points = IngredientPoint(
        vgr=14,
        sprt=23,
        soph=18,
    )
    synergies: List[BaseSynergy] = []


class KingSquid(Ingredient):
    name = "King Squid"
    name_ru = "Королевский кальмар"
    tags: List[Tag] = [Tag.sea, Tag.animal]
    points = IngredientPoint(
        vgr=21,
        sprt=25,
        soph=4,
    )
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=52,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.mixed, Tag.plant])],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=0, soph=45))]
        ),
        AllConditionsSynergy(
            min_level=2,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.land, Tag.magic])],
            mechanics=[
                MultiplierSynergyMechanic(bonuses=BasePoint(vgr=2.4, sprt=0, soph=0)),
                MultiplierSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=2, soph=0))
            ]
        )
    ]


class ToastedCuttlefish(Ingredient):
    name = "Toasted Cuttlefish"
    name_ru = "Жареная каракатица"
    tags: List[Tag] = [Tag.sea, Tag.animal]
    points = IngredientPoint(
        vgr=16,
        sprt=11,
        soph=28,
    )
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=56,
            conditions=[SpecificIngredientRequired(ingredient="Queen Carp")],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=50, sprt=0, soph=0))]
        ),
        AllConditionsSynergy(
            min_level=2,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.mixed, Tag.animal])],
            mechanics=[MultiplierSynergyMechanic(bonuses=BasePoint(vgr=3, sprt=0, soph=0))]
        )
    ]


class Thunander(Ingredient):
    name = "Thunander"
    name_ru = "Громунец"
    tags: List[Tag] = [Tag.sea, Tag.animal]
    points = IngredientPoint(
        vgr=15,
        sprt=15,
        soph=25,
    )
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=54,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.land, Tag.animal])],
            mechanics=[
                FlatSynergyMechanic(bonuses=BasePoint(vgr=20, sprt=0, soph=0)),
                MultiplierSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=3.2, soph=0))
            ]
        ),
        AllConditionsSynergy(
            min_level=2,
            conditions=[MustBeFirstIngredient()],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=37, soph=0))]
        )
    ]


class FireGoldfish(Ingredient):
    name = "Fire Goldfish"
    name_ru = "Огненная золотая рыбка"
    tags: List[Tag] = [Tag.sea, Tag.magic]
    points = IngredientPoint(
        vgr=9,
        sprt=3,
        soph=8,
    )
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=2,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.sea, Tag.magic])],
            mechanics=[MultiplierSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=1.8, soph=0))]
        )
    ]


class Boltuna(Ingredient):
    name = "Boltuna"
    name_ru = "Молтунец"
    tags: List[Tag] = [Tag.sea, Tag.magic]
    points = IngredientPoint(
        vgr=2,
        sprt=11,
        soph=7,
    )
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=2,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.land, Tag.magic])],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=15, soph=0))]
        ),
        AllConditionsSynergy(
            min_level=2,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.mixed, Tag.plant])],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=0, soph=15))]
        )
    ]


class SweetCuttlefish(Ingredient):
    name = "Sweet Cuttlefish"
    name_ru = "Сладкая каракатица"
    tags: List[Tag] = [Tag.sea, Tag.magic]
    points = IngredientPoint(
        vgr=14,
        sprt=19,
        soph=7,
    )
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=2,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.land, Tag.plant])],
            mechanics=[
                MultiplierSynergyMechanic(bonuses=BasePoint(vgr=2.4, sprt=0, soph=0)),
                MultiplierSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=1.8, soph=0))
            ]
        )
    ]


class GoldenJellyfish(Ingredient):
    name = "Golden Jellyfish"
    name_ru = "Золотая медуза"
    tags: List[Tag] = [Tag.sea, Tag.magic]
    points = IngredientPoint(
        vgr=13,
        sprt=13,
        soph=14,
    )
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=41,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.land, Tag.magic])],
            mechanics=[MultiplierSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=3, soph=0))]
        ),
        AllConditionsSynergy(
            min_level=2,
            conditions=[MustBeFirstIngredient()],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=9, sprt=16, soph=13))]
        )
    ]


class Triclopus(Ingredient):
    name = "Triclopus"
    name_ru = "Триклоп"
    tags: List[Tag] = [Tag.sea, Tag.magic]
    points = IngredientPoint(
        vgr=18,
        sprt=18,
        soph=14,
    )
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=2,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.land, Tag.magic])],
            mechanics=[MultiplierSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=0, soph=3.4))]
        ),
        AllConditionsSynergy(
            min_level=50,
            conditions=[MustBeFirstIngredient()],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=35, sprt=0, soph=0))]
        )
    ]


class RicePasta(Ingredient):
    name = "Rice Pasta"
    name_ru = "Рисовая паста"
    tags: List[Tag] = [Tag.mixed, Tag.plant]
    points = IngredientPoint(
        vgr=1,
        sprt=18,
        soph=11,
    )
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=33,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.sea, Tag.magic])],
            mechanics=[MultiplierSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=0, soph=2.5))]
        ),
        AllConditionsSynergy(
            min_level=2,
            conditions=[MustBeFirstIngredient()],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=32, soph=0))]
        )
    ]


class GroundBeef(Ingredient):
    name = "Ground Beef"
    name_ru = "Говяжий фарш"
    tags: List[Tag] = [Tag.mixed, Tag.animal]
    points = IngredientPoint(
        vgr=12,
        sprt=12,
        soph=8,
    )
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=14,
            conditions=[SpecificIngredientRequired(ingredient="Crab")],
            mechanics=[MultiplierSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=2, soph=0))]
        ),
        AllConditionsSynergy(
            min_level=2,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.sea, Tag.plant])],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=15, sprt=0, soph=0))]
        )
    ]


class Surimi(Ingredient):
    name = "Surimi"
    name_ru = "Сурими"
    tags: List[Tag] = [Tag.mixed, Tag.animal]
    points = IngredientPoint(
        vgr=6,
        sprt=13,
        soph=6,
    )
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=21,
            conditions=[SpecificIngredientRequired(ingredient="Mud Eel")],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=27, sprt=0, soph=0))]
        ),
        AllConditionsSynergy(
            min_level=13,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.sea, Tag.animal])],
            mechanics=[MultiplierSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=0, soph=1.9))]
        )
    ]


class PinkDough(Ingredient):
    name = "Pink Dough"
    name_ru = "Розовое тесто"
    tags: List[Tag] = [Tag.mixed, Tag.magic]
    points = IngredientPoint(
        vgr=13,
        sprt=11,
        soph=11,
    )
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=2,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.land, Tag.plant])],
            mechanics=[MultiplierSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=2, soph=0))]
        ),
        AllConditionsSynergy(
            min_level=2,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.sea, Tag.animal])],
            mechanics=[MultiplierSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=2, soph=0))]
        ),
        AllConditionsSynergy(
            min_level=28,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.mixed, Tag.animal])],
            mechanics=[MultiplierSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=0, soph=1.8))]
        )
    ]


class BreadedErwin(Ingredient):
    name = "Breaded Erwin"
    name_ru = "Панированный эрвинов плод"
    tags: List[Tag] = [Tag.mixed, Tag.magic]
    points = IngredientPoint(
        vgr=18,
        sprt=2,
        soph=10,
    )
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=32,
            conditions=[SpecificIngredientRequired(ingredient="Depths Crab")],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=0, soph=18))]
        ),
        AllConditionsSynergy(
            min_level=30,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.mixed, Tag.animal])],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=28, sprt=0, soph=0))]
        )
    ]


class PangunGhost(Ingredient):
    name = "Pangun Ghost"
    name_ru = "Призрак пангуна"
    tags: List[Tag] = [Tag.mixed, Tag.magic]
    points = IngredientPoint(
        vgr=6,
        sprt=13,
        soph=21,
    )
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=57,
            conditions=[SpecificIngredientRequired(ingredient="Hypnofish")],
            mechanics=[
                FlatSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=0, soph=50)),
                MultiplierSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=3.6, soph=0))
            ]
        ),
        AllConditionsSynergy(
            min_level=2,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.land, Tag.plant])],
            mechanics=[MultiplierSynergyMechanic(bonuses=BasePoint(vgr=2, sprt=0, soph=0))]
        )
    ]


class BreadedSpiderLeg(Ingredient):
    name = "Breaded Spider Leg"
    name_ru = "Паучья лапа в панировке"
    tags: List[Tag] = [Tag.mixed, Tag.magic]
    points = IngredientPoint(
        vgr=32,
        sprt=15,
        soph=13,
    )
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=30,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.sea, Tag.animal])],
            mechanics=[
                FlatSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=35, soph=0)),
                FlatSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=0, soph=35))
            ]
        ),
        AllConditionsSynergy(
            min_level=47,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.sea, Tag.magic])],
            mechanics=[MultiplierSynergyMechanic(bonuses=BasePoint(vgr=4, sprt=0, soph=0))]
        )
    ]


class EtherealKatsuobushi(Ingredient):
    name = "Ethereal Katsuobushi"
    name_ru = "Эфирные кацуобуси"
    tags: List[Tag] = [Tag.mixed, Tag.magic]
    points = IngredientPoint(
        vgr=20,
        sprt=30,
        soph=20,
    )
    synergies: List[BaseSynergy] = [
        AllConditionsSynergy(
            min_level=58,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.mixed, Tag.plant])],
            mechanics=[
                MultiplierSynergyMechanic(bonuses=BasePoint(vgr=2, sprt=0, soph=0)),
                MultiplierSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=0, soph=2)),
                MultiplierSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=2, soph=0))
            ]
        ),
        AllConditionsSynergy(
            min_level=45,
            conditions=[PreviousIngredientsHaveAllTags(tags=[Tag.land, Tag.magic])],
            mechanics=[FlatSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=38, soph=0))]
        ),
        AllConditionsSynergy(
            min_level=2,
            conditions=[SpecificIngredientRequired(ingredient="Spider Silk")],
            mechanics=[
                MultiplierSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=2.8, soph=0)),
                MultiplierSynergyMechanic(bonuses=BasePoint(vgr=0, sprt=0, soph=2.8))
            ]
        )
    ]
