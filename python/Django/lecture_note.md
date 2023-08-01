# Django

> [Django 공식 홈페이지](https://www.djangoproject.com/)

## 장고앱 만드는 방법

1. 프로젝트 생성
2. 앱 생성
3. 프로젝트 설정 파일(settings.py) 변경
   - INSTALLED_APPS에 2번에서 만든 앱 추가
4. 필요한 앱 개발
   - URL 설계(local url ➡️ urls.py)
   - view 개발(비즈 로직=BE 개발)(app.py)
   - template 개발(FE 개발)(templates/\*.html)
   - model 개발(DB 개발)(models.py)
5. 메인 프로젝트와 앱 연결
   - 메인 프로젝트 URL과 앱 URL 연결
6. 배포/운영 셋업
   - DEBUG 모드 끄기
   - 실행 (python manage.py runserver)

```bash
django-admin startproject HelloWorldProject
python manage.py startapp helloworldapp
# django-admin startapp helloworldapp
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

## model 만들기

- models.py에 정의
- 마이그레이션

```bash
python manage.py makemigrations
python manage.py migrate
```

## DB 접근이 가능한(쓸데없는🤣) 인터페이스(파이썬 shell open)

- 장고 프로젝트에 관련한 파이썬 shell을 열어줘서 코드 입력으로 test, 디버깅 가능

```bash
python manage.py shell

from helloapp.models import Message
messages = Message.objects.all()
print(messages)
# ❓ 아래 안녕하세요라고 나오는 건 models 클래스에서 str 함수 구현했기 때문
<QuerySet [<Message: 안녕하세요>]>
new_message = Message(text='안녕히가세요')
new_message.save()

message_to_delete = Message.objects.get(id=3)
message_to_delete = Message.objects.filter(text='안녕~~~')
message_to_delete.delete()
```
