from flask import Flask, render_template, request, redirect, session, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = "this_is_my_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
# 실시간 동기화하지 않고, 내가 원할 때 테이블에 데이터를 기록하고 commit()하는 형태
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email

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

@app.route('/view')
def view():
    return render_template("view.html", users=Users.query.all())

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # DB를 통해서 로그인 확인 - 지금은 가상 테이블
        found_user = Users.query.filter_by(name=username).first()
        if found_user:
            flash("Login Successful")
        else:
            user = Users(username, password, "")
            db.session.add(user)
            db.session.commit()
            flash("User Create")
        
        session['username'] = username
        return redirect(url_for('home'))

    return render_template('login.html')

@app.route('/delete', methods = ['POST'])
def delete():
    user = session['username']

    if request.method == 'POST':
        action = request.form["action"]
        if action == "DELETE":
            Users.query.filter_by(name=user).delete()
            db.session.commit()
            return redirect(url_for('logout'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8080)