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
    'sphinx.ext.autosummary',
    'nbsphinx',
]
system_packages: true



#templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
#html_static_path = ['_static']
