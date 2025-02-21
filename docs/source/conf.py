# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# conf.py

# Path to your Python modules
import os
import sys
sys.path.insert(0, os.path.abspath('../../'))  # Adjust this path if necessary


project = 'PAsampling'
copyright = '2025, Paolo Climaco'
author = 'Paolo Climaco'
version = '0.0.1'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add 'sphinx.ext.autodoc' to the extensions list

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.napoleon',  # For Google-style docstrings
    'sphinx.ext.viewcode',  # To link to source code in docs
    'sphinx.ext.autodoc',
     'sphinx.ext.mathjax',
    'sphinx.ext.autosummary',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'nbsphinx',
]


html_context = {
    "display_github": True, # Integrate GitHub
    "github_user": "PaClimaco", # Username
    "github_repo": "PAsampling", # Repo name
    "github_version": "master", # Version
    "conf_py_path": "/docs/source/", # Path in the checkout to the docs root
}



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Sphinx configuration may also need to include directories where content is stored
source_suffix = '.rst'  # or '.md', depending on your documentation source
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


html_theme = 'sphinx_rtd_theme'
#html_static_path = ['_static']
