from setuptools import find_packages
from setuptools import setup

setup(
    name='vision',
    version='0.0.0',
    packages=find_packages(
        include=('vision', 'vision.*')),
)
