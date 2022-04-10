"""Sphinx configuration."""
from datetime import datetime


project = "Design_Patterns_In_Python"
author = "Taras Shevchenko"
copyright = f"{datetime.now().year}, {author}"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
]
autodoc_typehints = "description"
html_theme = "furo"
