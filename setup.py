from os.path import join, dirname
from setuptools import setup, find_packages

import djangix

setup(
    name="djangix",
    version=djangix.__version__,
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    long_description=open(join(dirname(__file__), "README.md")).read(),
    install_requires=["unidecode"],
)
