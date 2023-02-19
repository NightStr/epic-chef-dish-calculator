from typing import List

from dish.base import Ingredient, BaseSynergyCondition
from dish.tags import Tag


class PreviousIngredientsHaveAllTags(BaseSynergyCondition):
    tags: list[Tag]

    def can_apply(self, ingredients: List[Ingredient]) -> bool:
        exists_tags = []
        for i in ingredients:
            exists_tags.extend(i.tags)
        return all(tag in exists_tags for tag in self.tags)


class MustBeFirstIngredient(BaseSynergyCondition):
    def can_apply(self, ingredients: List[Ingredient]) -> bool:
        return not ingredients


class SpecificIngredientRequired(BaseSynergyCondition):
    ingredient: str

    def can_apply(self, ingredients: List[Ingredient]) -> bool:
        return any(self.ingredient == i.name for i in ingredients)
