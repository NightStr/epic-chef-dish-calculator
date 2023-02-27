from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


# определяем модель для таблицы dishes
class Dish(Base):
    __tablename__ = 'dishes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    vgr = Column(Float)
    sprt = Column(Float)
    soph = Column(Float)
    required_level = Column(Integer)
    sum_points = Column(Float)
    ingredient_1_name = Column(String)
    ingredient_1_name_ru = Column(String)
    ingredient_2_name = Column(String)
    ingredient_2_name_ru = Column(String)
    ingredient_3_name = Column(String)
    ingredient_3_name_ru = Column(String)
    ingredient_4_name = Column(String)
    ingredient_4_name_ru = Column(String)
    tags = Column(String)
