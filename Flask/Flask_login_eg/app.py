from flask import Flask, render_template, request, redirect, session, url_for, flash

app = Flask(__name__)

app.secret_key = "this_is_my_secret_key"

# 가상의 사용자 테이블
users = {
    'user1' : {'password': 'password123'},
    'user2' : {'password': 'abc123'}
}

@app.route('/')
def home():
    if 'username' in session:
        flash("Login에 성공하였습니다.")
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # DB를 통해서 로그인 확인 - 지금은 가상 테이블
        if username in users and users[username]['password'] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            # 카테고리 넣을 수 있음
            flash("Login에 실패하였습니다.")

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

# 미션1 : render_template 통해서 첫 화면에 login/logout 추가
# 미션2 : 로그인 성공, 실패 여부를 flash 메시지 통해서 처리
# 미션3 : 디자인 적용해서 flash 메시지 색상 다르게 해보기(성공시 초록, 실패시 빨강)

if __name__ == "__main__":
    app.run(debug=True, port=8080)