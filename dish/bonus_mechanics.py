from dish.base import BasePoint, DishPoint, BaseSynergyMechanic


class FlatSynergyMechanic(BaseSynergyMechanic):
    bonuses: BasePoint

    def apply(self, dish_points: DishPoint) -> DishPoint:
        return dish_points + self.bonuses


class MultiplierSynergyMechanic(BaseSynergyMechanic):
    bonuses: BasePoint

    def apply(self, dish_points: DishPoint) -> DishPoint:
        return dish_points * BasePoint(
            vgr=self.bonuses.vgr or 1,
            sprt=self.bonuses.sprt or 1,
            soph=self.bonuses.soph or 1
        )
