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

## 🎆 이미지 업로드

### DB

- 디스크의 파일 경로(path / 서버에 바이너리 데이터를 저장하기 위한 공간) / 파일의 정보만 저장
- AWS ➡️ S3 저장소
- 플랫폼의 링크(유튜브...)

### 기본 경로 셋업

```python
# 📂 settings.py

# ✨ 우리 프로젝트 전체의 미디어 업로드 폴더 생성
MEDIA_ROOT = os.path.join(BASE_DIR, 'upload')

# ✨ 웹 컴포넌트가 이 미디어 폴더를 어떤 URI로 접근할건지
MEIDA_URL = '/media/'

# 📂 프로젝트 ➡️ urls.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### 라이브러리 설치

```bash
# 이미지 파일을 관리하는 라이브러리
python -m pip install Pillow
```

### model 만들기

```python
# 📂 models.py
from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=200, blank=False)
    # DB에는 경로에 대한 url이 들어가고, 사진은 photos/ 폴더를 만들어서 업로드
    image = models.ImageField(upload_to='photos/', null=False)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

### html에서 불러오기

```html
<!-- {{ photo.image.url }}로 path 불러옴 -->
{% for photo in photos %}
<li>
  <div>Title : {{ photo.title }}</div>
  <img src="{{ photo.image.url }}" alt="{{ photo.title }}" />
  <div>업로드 일자 : {{ photo.upload_date }}</div>
</li>
{% endfor %}
```
