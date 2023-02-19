from typing import List

from dish.base import Ingredient, BaseExtraBonus


class AllConditionsExtraBonus(BaseExtraBonus):
    def can_apply(self, player_level: int, ingredients: List[Ingredient]) -> bool:
        return super().can_apply(player_level, ingredients) and all((c.can_apply(ingredients) for c in self.conditions))


class OnlyOneConditionExtraBonus(BaseExtraBonus):
    def can_apply(self, player_level: int, ingredients: List[Ingredient]) -> bool:
        return super().can_apply(player_level, ingredients) and any((c.can_apply(ingredients) for c in self.conditions))
