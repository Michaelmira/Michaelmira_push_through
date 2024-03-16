import os
import sys

from setuptools import find_packages, setup
sys.path.append(os.path.dirname(__file__))

__version__ = "0.0.1"

setup(
    name="push_through",
    version=__version__,
    description="Push Through - Connect4 on Steroids",
    author="Caballero Coding Company",
    author_email="michaelmirisciotta@gmail.com",
    python_requires=">=3.9",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
)