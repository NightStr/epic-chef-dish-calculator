from dish.base import BasePoint, DishPoint, BaseBonusMechanic


class FlatBonusMechanic(BaseBonusMechanic):
    bonuses: BasePoint

    def apply(self, dish_points: DishPoint) -> DishPoint:
        return dish_points + self.bonuses


class MultiplierBonusMechanic(BaseBonusMechanic):
    bonuses: BasePoint

    def apply(self, dish_points: DishPoint) -> DishPoint:
        return dish_points * self.bonuses


class AddAndThenMultiplyBonusMechanic(BaseBonusMechanic):
    add_bonuses: BasePoint
    multiply_bonuses: BasePoint

    def apply(self, dish_points: DishPoint) -> DishPoint:
        return (dish_points + self.add_bonuses) * self.multiply_bonuses
