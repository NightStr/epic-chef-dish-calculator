from typing import List, Type

from dish.base import Ingredient, BaseBonusCondition
from dish.tags import Tag


class PreviousIngredientsHaveAllTags(BaseBonusCondition):
    tags: list[Tag]

    def can_apply(self, ingredients: List[Ingredient]) -> bool:
        exists_tags = []
        for i in ingredients:
            exists_tags.extend(i.tags)
        return all(tag in exists_tags for tag in self.tags)


class HaveNoPreviousIngredients(BaseBonusCondition):
    def can_apply(self, ingredients: List[Ingredient]) -> bool:
        return not ingredients


class HaveIngredientInIngredients(BaseBonusCondition):
    ingredient: Type[Ingredient]

    def can_apply(self, ingredients: List[Ingredient]) -> bool:
        return any(isinstance(i, self.ingredient) for i in ingredients)
