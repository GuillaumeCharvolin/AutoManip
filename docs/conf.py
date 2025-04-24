# docs/conf.py
import os
import sys
# If your project code needs to be importable for autodoc, uncomment this:
# sys.path.insert(0, os.path.abspath('../src')) # Adjust path as needed

# -- Project information -----------------------------------------------------
project = 'AutoManip'
copyright = '2025, Your Name or Organization' # Update copyright
author = 'Your Name or Organization'          # Add author
# release = '0.1.0' # Consider adding a version

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',    # Include documentation from docstrings
    'sphinx.ext.napoleon',   # Support for Google and NumPy style docstrings
    'sphinx.ext.viewcode',   # Add links to source code
    'sphinx.ext.githubpages',# Support for GitHub Pages
    'myst_parser',           # Enable Markdown parsing
    # Add other Sphinx extensions here if needed
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Source file parsers for different extensions
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'  # Or choose another theme like 'sphinx_rtd_theme', 'furo', etc.
# html_static_path = ['_static'] # If you have custom static files

# -- MyST Parser configuration -----------------------------------------------
# See https://myst-parser.readthedocs.io/en/latest/syntax/optional.html
myst_enable_extensions = [
    "admonition",      # Corresponds to admonitions
    "colon_fence",     # Needed for directives like .. code-block::, admonitions etc.
    "amsmath",         # For math blocks (may need latex installed for PDF build) - like arithmatex
    "dollarmath",      # To allow $...$ and $$...$$ math - like arithmatex
    "smartquotes",     # Like pymdownx.smartsymbols
    "tasklist",        # Like pymdownx.tasklist (requires Extended Syntax enabled)
    "html_admonition", # Allows using HTML <details> for admonitions
    "deflist",         # Definition lists
    "linkify",         # Auto-detect links like www.example.com
    "substitution",    # Allows replacements like |project|
    "attrs_inline",    # Allows inline attributes like {style="color: red"}
    "attrs_block",     # Allows block-level attributes
    # Note: Code highlighting is handled by Sphinx/Pygments, not a specific MyST extension (usually enabled by default).
    # Note: Footnotes are standard in MyST.
    # Note: 'betterem', 'caret', 'critic', 'details', 'emoji', 'inlinehilite', 'keys', 'mark', 'tilde' from pymdownx
    #       may not have direct equivalents or might be covered by other extensions or standard MyST/Sphinx features.
    #       Review the MyST documentation for equivalents if specific features are crucial.
    #       For example, emoji might need a separate sphinx extension like sphinxemoji
]

# Optional: Enable extended syntax for tasklists, etc.
# myst_enable_extended_syntax = True # Tasklist might need this, check MyST docs

# Optional: Configure code highlighting (handled by Pygments via Sphinx)
pygments_style = 'sphinx' # Or 'friendly', 'monokai', etc.

# -- Options for LaTeX/PDF output ---------------------------------------------
# (Required if you build PDF format)
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'AutoManip.tex', 'AutoManip Documentation',
   author, 'manual'), # Make sure 'index' is your main landing page (index.md or index.rst)
]