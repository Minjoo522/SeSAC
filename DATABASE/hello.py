import sqlite3

# DB에 접속
conn = sqlite3.connect('hello.db') # sqlite 파일 확장자는 일반적으로 .sqlite / .sqlite3

# conn을 통해 메시지를 주고 받음
# 로우레벨 접속을 한 소켓 인터페이스
# 커서(cursor, 명령어를 주고받는 위치)
c = conn.cursor()

user_input = "user2"
pass_input = "abcd2222"
# query = "SELECT * FROM users WHERE username=" + user_input

# c.execute("SELECT * FROM users WHERE username=? AND password=?", (user_input, pass_input))
# result = c.fetchall() # 가져오는 것
# result = c.fetchone() # 결과 하나만 갖고 오는 것
# result = c.fetchmany(2) # 원하는 개수만큼 갖고 오는 것
# for r in result:
#     print(r)

# 미션, 로그인 코드를 구현한다
def login(user_input, pass_input):
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (user_input, pass_input))
    result = c.fetchall() 

    if len(result) == 1:
        print("로그인에 성공하였습니다.")
    else:
        print("로그인에 실패하였습니다.")

login(user_input, pass_input)

# DB 사용이 다 끝났을 때, 변경 사항들을 최종 기록
# 변경 사항이 없는 경우 commit 하지 않아도 됨
conn.commit()

# 접속 종료
# 프로그램이 종료되기 위해서 자동 종료 되지만, 안정적으로 프로그램을 운영하기 위해서 어디엔가는 존재해야 한다
conn.close()

# 미션✨, 암호화(단방향 암호화인 HASH) 처리해서 로그인 하는 코드 구현하기 
username = input("사용자 이름을 입력하세요: ")
password = input("비밀번호를 입력하세요: ")

def login