#!/usr/bin/env python

import codecs
from setuptools import setup

# Version info -- read without importing
_locals = {}
with open("alabaster/_version.py") as fp:
    exec(fp.read(), None, _locals)
version = _locals["__version__"]

# README into long description
with codecs.open("README.rst", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="aioli_sphinx_theme",
    version=version,
    description="A configurable sidebar-enabled Sphinx theme",
    long_description=readme,
    author="Jeff Forcier",
    author_email="jeff@bitprophet.org",
    url="https://alabaster.readthedocs.io",
    packages=["alabaster"],
    include_package_data=True,
    entry_points={"sphinx.html_themes": ["aioli_sphinx_theme = alabaster"]},
)
