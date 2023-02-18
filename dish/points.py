from dataclasses import dataclass

from dish.base import Ingredient, BaseIngredient


@dataclass
class BasePoint:
    vgr: int
    sprt: int
    soph: int


@dataclass
class IngredientPoint(BasePoint):
    ...


@dataclass
class DishPoint(BasePoint):
    def copy(self) -> "DishPoint":
        return DishPoint(
            vgr=self.vgr,
            sprt=self.sprt,
            soph=self.soph
        )

    def add_ingredient(self, ingredient: BaseIngredient) -> "DishPoint":
        return DishPoint(
            vgr=self.vgr + ingredient.points.vgr,
            sprt=self.sprt + ingredient.points.sprt,
            soph=self.soph + ingredient.points.soph
        )
