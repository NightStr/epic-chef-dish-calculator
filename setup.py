from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='epic-chef-dish-calculator',
    ext_modules=cythonize(['main.py'])
)
