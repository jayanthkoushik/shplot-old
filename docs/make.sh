#!/usr/bin/env sh
# Usage: docs/make.sh  # must be executed from the project root

sphinx-apidoc \
    -o docs/_build \
    -d 1 \
    --module-first \
    --tocfile index \
    --separate \
    src/*

sphinx-build \
    -C \
    -D extensions=sphinx.ext.autodoc,sphinx.ext.napoleon \
    -D default_role=samp \
    -D autodoc_member_order=bysource \
    -D autodoc_typehints=description \
    -D highlight_language=python \
    -b markdown \
    -c docs \
    -d docs/_build/.doctrees \
    docs/_build docs $(ls docs/_build/*.rst)

# Remove trailing spaces from generated files.
find docs -name '*.md' -exec perl -pi -e 's/ *$//' {} +
