# Flask 중급

## flask run으로 실행 가능 => app.py 실행 됨

## app.py 없는 경우 export FLASK_APP = myapp.py(고정적으로 설정 / 리눅스)와 같이 메인 앱 실행 파일 정의 후 flask run

- FLASK_APP : 환경 변수(environment variable)
- FLASK_APP = myapp.py flask run과 같이 리눅스는 한시적(temporarilily)으로 바로 실행 가능
- app.run() 괄호 안에 다양한 config(애플리케이션을 실행 할 때의 옵션 값) 옵션 정의 할 수 있음.
- flask run --debug, flask run -d : 디버그 옵션
- flask run --host=0.0.0.0 --port=5000과 같이 개발 서버 실행 옵션도 설정 가능
  - flask는 WAS 기능을 제공해주는 것이라서 WEB 서버 기능은 없음 : 이럴 때 host=0.0.0.0 굳이 할 필요가 없음 그래서 저런 실행 옵션이 있는 것!
  - 실무에서는 nginx, gunicorn 별도의 웹서버를 통해서 구동함

## 세션 관리

- TCP : 상태 있음, stateful / HTTP도 TCP 기반(GET, POST)
- UDP : 상태 없음, stateless
- 과거에 stateless 할 때는 필요 없었던 정보를 저정하기 위한 공간이 필요해짐
  - 클라이언트 사이드 : 우리의 PC, 사용자 환경 / **_쿠키_**
  - 서버 사이드 : 서버(웹서버/WAS 서버) / **_세션_**
- 세션 ID를 기반으로 내가 원하는 데이터 뭐든지 저장 가능(용량에 대한 제약이 있긴함)
- 세션의 ID 값은 쿠키를 통해서 클라이언트 사이드에 저장 됨
- 장시간 오랫동안 보관해야 하는 정보인 경우 : db 안에 세션 정보를 저장
- flask의 config 객체를 통해 PERMANENT_SESSION_LIFETIME(만료 시간)을 설정할 수 있음

### 세션ID <- 기본적으로 브라우저가 종료될 때 삭제 됨

- 개발자 도구의 쿠키의 value에서 확인 가능

## 실습

```python
# get parameter 처리
@app.route('/')
def user():
    name = request.args.get('name')
    return render_template("index.html", name=name)

# 여러개 처리도 가능
def user():
    name = request.args.get('name')
    age = request.args.get('age')

    return render_template("index.html", name=name, age=age)
```

## flash

- 비동기적으로 생성되는 메세지 처리
- 임시적인 데이터를 보내서 처리하는 것
- 백그라운드로 처리되는 결과들을 다시 FE 보내줄 때

```python
# 📂 python

@app.route('/')
def home():
    if 'username' in session:
        flash("Login에 성공하였습니다.")
    return render_template('index.html')
```

```html
<!-- 📂 html -->

{% with messages = get_flashed_messages() %} {% if messages %} {% for message in messages %}
<!-- ✨ for category, message in messages로 하면 category도 출력 가능 -->
<div class="alert alert-success alert-dismissible fade show" role="alert">
  <p>{{ message }}</p>
  <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
</div>
{% endfor %} {% endif %} {% endwith %}
```
