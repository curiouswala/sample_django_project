#!/usr/bin/env bash

# clean old build
rm -r dist libraryproject.pyz

# include the dependencies
pip install -r requirements.txt --target dist/

# specify which files to be included in the build
cp -r \
-t dist \
sample_app sample_django_project manage.py db.sqlite3

# build!
shiv --site-packages dist --compressed -p '/usr/bin/env python3' -o sample_django_project.pyz -e sample_django_project.main