from dish.base import BasePoint, DishPoint, BaseBonusMechanic


class FlatBonusMechanic(BaseBonusMechanic):
    bonuses: BasePoint

    def apply(self, dish_points: DishPoint) -> DishPoint:
        return dish_points + self.bonuses


class MultiplierBonusMechanic(BaseBonusMechanic):
    bonuses: BasePoint

    def apply(self, dish_points: DishPoint) -> DishPoint:
        return dish_points * BasePoint(
            vgr=self.bonuses.vgr or 1,
            sprt=self.bonuses.sprt or 1,
            soph=self.bonuses.soph or 1
        )
