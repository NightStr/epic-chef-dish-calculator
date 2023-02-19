from typing import List

from dish.base import Ingredient, BaseSynergy


class AllConditionsSynergy(BaseSynergy):
    def can_apply(self, player_level: int, ingredients: List[Ingredient]) -> bool:
        return super().can_apply(player_level, ingredients) and all((c.can_apply(ingredients) for c in self.conditions))


class OnlyOneConditionSynergy(BaseSynergy):
    def can_apply(self, player_level: int, ingredients: List[Ingredient]) -> bool:
        return super().can_apply(player_level, ingredients) and any((c.can_apply(ingredients) for c in self.conditions))
