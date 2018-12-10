# Notes

## Django Commands Usage

### Create a Project

```zsh
django-admin startproject <projectname>
```

If you are in the directory `django`, run
```zsh
django-admin startproject mysite
```
will create the following files:

```
django/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

Here,
* [`manage.py`][django-admin]: command-line utility that lets you interact with this Django project in various ways.
* `mysite/`: actual Python package for your project.
* `mysite/__init__.py`: empty file that makes `mysite/` a Python package.
* `mysite/settings.py`: settings/configuration for this Django project.
* `mysite/urls.py`: the URL declarations for this Django project; a "table of contents" of your Django-powered site.
* `mysite/wsgi.py`: an entry-point for WSGI-compatible web servers to serve your project.

[django-admin]: https://docs.djangoproject.com/en/2.1/ref/django-admin/

### Start the Development Server

```zsh
python manage.py runserver
```

If you want to change the server's port, pass it as a command-line argument, e.g.:
```zsh
python manage.py runserver 8080
```

### Create an App

In the directory that contains `manage.py`, run
```zsh
python manage.py startapp <appname>
```
where `appname` is the name of the application you want to add. For example,
```zsh
python manage.py startapp logs
```
will create a directory `logs` in `django` with the following layout:
```
logs/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

### Create a Superuser

```zsh
python manage.py createsuperuser
```
You may need to supply an username, an email, and a password.

### Migrate the Models

```zsh
python manage.py makemigrations [<app_name>]
```
creates new migrations based on the changes detected to your models.

### Synchronize the Database with Models

```zsh
python manage.py migrate
```
synchronizes the database state with the current set of models and migrations.

## Django Basics

**Points:**
* Fields are specified by class attributes. They are the only required part of a model defining the database fields.
* Built-in field types: TODO:

## Misc

* Superuser name: `DeepWalter`
* Password: `have fun`