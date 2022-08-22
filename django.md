#check if we have python

1- python --version

# create ENV

2- python -m venv env

#activate env

3- source env/Scripts/Activate (for bash) => return env if env is formed

# check dependencies

4- pip freeze

5- pip install django

If we pull someones project from git we need to install the dependencies => pip install -r requirements.txt (or what the package.JSON equilavents name)

# check dependencies again should see django

6- pip freeze

# project creation

7- django-admin startproject projectname .

After creating the project we must save it inside settings.py INSTALLED_APPS array under the server folder

#running

8- python manage.py runserver

#creating app

9- python manage.py startapp appname
