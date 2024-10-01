# Installing Django on PythonAnywhere

## PythonAnywhere
PythonAnywhere is a hosting enviornment

### Consoles
Access the only free machine provided by pythonAnywhere through bash

### Files
You can see and edit files on your remote system

### Web
To basically host your app

## Create a virtual enviornment
(I was already familiar with linux commands, so not mentioning those here)

run `mkvirtualenv django5`. it will create and activate the enviornment. Download django there through pip. (I am personally using [uv](https://github.com/astral-sh/uv)). Just make sure you are in the created enviornment, there will be (django5) written before the bash prompt.

If you want this env to be actvated by default when you open bash, just add `workon django5` at the end of the .bashrc file.

can't use sudo here 🥲, so python or uv venv will not work here

## First Django Project

1. Created a directory (django_projects)
2. created a project (mysite): `django-admin startproject mysite`
3. In home/_username_/django_projects/mysite/mysite/**settings.py** added `*` in allowed hosts e.g. `ALLOWED_HOSTS = ['*']`
    - here _python manage.py runserver_ will not work since its not your local machine and you will be accessing it through a valid url. Just run **_python manage.py check_** and it will let you know if you have any errors.
4. on PythonAnywhere go to **Web** tab
    - go to code section, in `source code` and `working directory` paste the path of your project and similarly the virtual env path.
    - edit WSGI in code section and put only this code in there (use nano, vi or the file tab of pythonAnywhere):
    ```
        import os
        import sys

        path = os.path.expanduser('~/django_projects/mysite')
        if path not in sys.path:
            sys.path.insert(0, path)
        os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
        from django.core.wsgi import get_wsgi_application
        from django.contrib.staticfiles.handlers import StaticFilesHandler
        application = StaticFilesHandler(get_wsgi_application())
    ```
5. click on "Reload _username_.pythonanywhere.com" on start of the page

and voila your first project is ready to be viewed on web anywhere through the link in point 5

### Creating an app within project

**Note:** After any change you make do the check thing and reload
1. create an app: `python manage.py startapp polls`
2. cd into this app directory and edit views.py, it should look something like this:
    ```
    from django.shortcuts import render
    from django.http import HttpResponse

    def polls_main(request):
        return HttpResponse("Hello, world. 86a8f059 is the polls index.")
    ```
3. create urls.py in polls:
    ```
    from django.urls import path
    from . import views

    urlpatterns = [
        path("", views.polls_main, name="polls-index"),
    ]
    ```
4. edit urls.py in main project, which means you have to come back one step and go into the folder named same as project name (basically where we edited the settings.py):
    ```
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path("polls/", include('polls.urls')),
        path("admin/", admin.site.urls),
    ]
    ```
