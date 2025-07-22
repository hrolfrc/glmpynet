# Configuration file for the Sphinx documentation builder.

project = 'glmpynet'
# noinspection PyShadowingBuiltins
copyright = '2025, Rolf Carlson'
author = 'Rolf Carlson'
release = '0.5.3'

import os
import sys
sys.path.insert(0, os.path.abspath('../glmpynet'))

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Extensions
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',  # For Google-style docstrings
    'sphinx_rtd_theme',
    'nbsphinx',
]

# Theme
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# nbsphinx settings
# nbsphinx_execute = 'never'  # Use pre-executed outputs for reproducibility
