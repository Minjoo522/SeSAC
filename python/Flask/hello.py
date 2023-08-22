from flask import Flask, url_for, redirect

app = Flask(__name__)
# app = Flask("고유식별자")
# 이 모듈이 실행될 때 자동으로 실행되는 모듈 = __name__
# 바꾸어도 되지만, 굳이 바꿀 필요 ❌

@app.route('/')
def home():
    return """
    <html>
    <head>
    <title>My Title</title>
    </head>
    <body>
    <h1>Hello sesac from flask</h1>
    <p>Welcome to Flask class</p>
    <a href="/user">유저 페이지로 가기</a>
    </body>
    </html>"""
# 서버를 통해서 내용을 전달 중 -> 사진을 전송하는 코드를 짜지 않았기 때문에 이미지 전송은 안된다!
# 해당 경로를 Flask가 접근하지 못함
# <a href="/user"> 나의 루트는 풀 주소를 쓸 필요는 없음

# 동적으로 변하는 변수 처리
@app.route("/user")
def user_none():
    return """
    <ul>
    <li><a href="/user/tom">tom</a></li>
    <li><a href="/user/john">john</a></li>
    <li><a href="/user/bill">bill</a></li>
    </ul>
    """

@app.route("/user/<name>")
def user(name):
    return f"""
    <html>
    <head>
    <title>User</title>
    </head>
    <body>
    <h1>여기는 {name}의 페이지</h1>
    <a href="/">홈으로!</a>
    <a href="/user">이전 페이지로 가기</a>
    </body>
    </html>"""

@app.route("/admin")
def admin():
    return redirect(url_for('/user', name="admin"))
# 다른 함수에 전달!

if __name__ == "__main__":
    app.run(host="0.0.0.0")