from setuptools import find_packages
from setuptools import setup

setup(
    name='the_vision',
    version='0.0.0',
    packages=find_packages(
        include=('the_vision', 'the_vision.*')),
)
