from typing import List

from dish.base import Ingredient, BaseExtraBonus


class AllConditionsExtraBonus(BaseExtraBonus):
    def can_apply(self, ingredients: List[Ingredient]) -> bool:
        return all((c.can_apply(ingredients) for c in self.conditions))


class OnlyOneConditionExtraBonus(BaseExtraBonus):
    def can_apply(self, ingredients: List[Ingredient]) -> bool:
        return any((c.can_apply(ingredients) for c in self.conditions))
