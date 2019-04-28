0.  mkdir profiles-rest-api && cd profiles-rest-api
1.  add virtual env - python -m virtualenv env37
2.  acivate virtual env -  .\env37\Scripts\activate
3.  install Django - pip install Django==2.2
4.  install django rest - pip install djangorestframework
5.  create statup project - django-admin.py startproject profiles_project
6.  go to new directory - cd profiles_project
7.  create api - python manage.py startapp profiles_api
8.  check installed available packages - pip freeze
9.  create requirement.txt file with all available installed packages - pip freeze > requirements.txt
10. run application - python manage.py runserver

11. to run migration - python manage.py makemigrations
12. confirm migration and create database - python manage.py migrate