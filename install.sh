#!/bin/bash
cd
user=$(whoami)
projectName="infoweb"
python -m venv $(projectName)
cd $(projectName)
source bin/activate
pip install django
pip install pillow
django-admin startproject website
git clone https://github.com/nederjair/$(projectName).git
cp websiteRoot/* website/
mv websiteRoot websiteRoot_bk
mv website websiteRoot
cd websiteRoot
python manage.py makemigrations
python manage.py migrate
