#!/bin/bash
cd
user=$(whoami)
projectName="infoweb"
git clone https://github.com/nederjair/${projectName}.git
python -m venv $projectName
cd $projectName
source bin/activate
pip install django
pip install pillow
django-admin startproject website
cp -r websiteRoot/* website/                                                                                           
mv websiteRoot websiteRoot_bk
mv website websiteRoot
cd websiteRoot
python manage.py makemigrations pages
python manage.py makemigrations quotes
python manage.py migrate
