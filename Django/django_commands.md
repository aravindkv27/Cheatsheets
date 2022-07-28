# Django

```
 Django is an full stack webframework which allows an rapid development of websites.
```

## Create an Virtual Environment

<br>


```
pip install virtualenv
virtulaenv myenv
myenv\Scripts\activate
deactivate
```



## Django Installation

```
 pip install django 
```

## Setting up a Project

```
django-admin startproject
```

## To run a project

```
python manage.py runserver
```

## Start an app

```
python manage.py startapp app_name
```

## Migrate the app

```
python manage.py migrate
```

## Making Migration after changing in models.py in App
```
python manage.py makemigrations main
```

## Applying Migration

- Applying the migration once the making migration completes

```
python manage.py migrate
```

## Shell

```
python manage.py shell
```