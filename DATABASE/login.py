import sqlite3
import hashlib

# DB에 접속
# conn = sqlite3.connect('hello.db') # sqlite 파일 확장자는 일반적으로 .sqlite / .sqlite3

# c = conn.cursor()
conn = sqlite3.connect('hello.db')
cursor = conn.cursor()

# 미션✨, 사용자 콘솔로부터 username과 password를 받아서 쿼리에서 동작하는 함수를 구현하시오
def login(username, password):
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = cursor.fetchall()

    if len(result) == 1:
        print("로그인에 성공하였습니다.")
    else:
        print("로그인에 실패하였습니다.")

# username = input("사용자 이름을 입력하세요: ")
# password = input("비밀번호를 입력하세요: ")
# login(username, password)

# 미션2✨, 암호화(단방향 암호화인 HASH) 처리해서 로그인 하는 코드 구현하기
def password_hash(password):
    hash_password = hashlib.sha256(password.encode()).hexdigest()
    return hash_password

def signup():
    username, password = get_info()
    hash_password = password_hash(password)
    # ? 들어간 것 : prepare statement
    cursor.execute("INSERT INTO users (username, password) VALUES(?, ?)", (username, hash_password))
    conn.commit()

def login_hash():
    username, password = get_info()
    hash_password = password_hash(password)

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hash_password))
    result = cursor.fetchall()

    if len(result) == 1:
        print("로그인에 성공하였습니다.")
    else:
        print("로그인에 실패하였습니다.")

def get_info():
    username = input("사용자 이름을 입력하세요: ")
    password = input("비밀번호를 입력하세요: ")
    return username, password

login_hash()
