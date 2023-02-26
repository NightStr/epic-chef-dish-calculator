from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table, UniqueConstraint, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


# определяем промежуточную таблицу для связи блюд и ингредиентов
class DishIngredient(Base):
    __tablename__ = 'dish_ingredient'
    dish_id = Column(Integer, ForeignKey('dishes.id'), primary_key=True)
    ingredient_id = Column(String, ForeignKey('ingredients.name'), primary_key=True)
    ord = Column(Integer, nullable=False, primary_key=True)

    # связь "многие-к-одному" с таблицей dishes
    dish = relationship('Dish', backref='dish_ingredient')

    # связь "многие-к-одному" с таблицей ingredients
    ingredient = relationship('Ingredient', backref='dish_ingredient')
    __table_args__ = (UniqueConstraint('dish_id', 'ingredient_id', 'ord'),)


# определяем модель для таблицы dishes
class Dish(Base):
    __tablename__ = 'dishes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    vgr = Column(Float)
    sprt = Column(Float)
    soph = Column(Float)
    required_level = Column(Integer)
    sum_points = Column(Float)

    # связь "многие-ко-многим" с таблицей ingredients
    ingredients = relationship('Ingredient', secondary=DishIngredient.__table__,
                               backref='dishes', order_by=DishIngredient.ord)



class IngredientTag(Base):
    __tablename__ = 'ingredient_tag'
    ingredient_id = Column(String, ForeignKey('ingredients.name'), primary_key=True)
    tag_id = Column(Integer, ForeignKey('tags.id'), primary_key=True)

    ingredient = relationship('Ingredient', backref='tags_association')
    tag = relationship('Tag', backref='ingredients_association')

    __table_args__ = (UniqueConstraint('ingredient_id', 'tag_id'),)


# определяем модель для таблицы tags
class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)


# определяем модель для таблицы ingredients
class Ingredient(Base):
    __tablename__ = 'ingredients'
    name = Column(String, primary_key=True)
    name_ru = Column(String)
    vgr = Column(Float)
    sprt = Column(Float)
    soph = Column(Float)

    # связь "многие-ко-многим" с таблицей tags
    tags = relationship('Tag', secondary="ingredient_tag", backref='ingredients')