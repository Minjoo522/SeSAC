# Django

> [Django 공식 홈페이지](https://www.djangoproject.com/)

```bash
django-admin startproject HelloWorldProject
python manage.py startapp helloworldapp
```

```python
# 📂 settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # ✨ 새로 만든 폴더 추가
    'helloworldapp',
]
```

## urls는 통합 urls.py에 넣어도 되고, 각각의 앱에서 urls.py를 만들어서 해도 됨

```python
# 📂 앱의 urls.py
from django.urls import path
from . import views

# Flask에서 @app.route('/')와 동일한 역할
urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]

# 📂 메인의 urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('helloworldapp.urls'))
]
```

## 실행

```bash
python manage.py runserver
```

## DB

```bash
python manage.py migrate
```

## create superuser

```bash
python manage.py createsuperuser
```

- DB setup 안하면 안됨

## admin 언어 바꾸기

```python
# 📂 settings.py
LANGUAGE_CODE = 'ko-kr'
```
