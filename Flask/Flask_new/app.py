from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'secret'
# session 만료
app.permanent_session_lifetime = timedelta(minutes=1)

@app.route('/', methods=["GET", "POST"])
def home():
    name = None
    age = None
    flash("메시지 테스트")
    if request.method == "GET":
        name = request.args.get('name')
        age = request.args.get('age')
    elif request.method == "POST":
        name = request.form["name"]
        # session에 저장
        session['userid'] = name
        # session 만료 관련 설정 - 안해도 되긴 함
        # session.permanent = True
        flash("Login에 성공하였습니다.")
        flash("메시지 플래슁 예제입니다")
    else:
        return "UNKNOWN METHOD"

    return render_template("index.html", name=name, age=age)

@app.route('/user')
def user():
    if "userid" in session:
        user = session['userid']
        return f"hello, {user}"
    else:
        return redirect(url_for('home'))

@app.route('/redirect')
def redirect_example():
    return redirect(url_for('user'))

if __name__ == "__main__":
    app.run(debug=True, port=8080)