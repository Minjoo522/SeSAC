import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect('user.db')
cursor = conn.cursor()

# 사용자 테이블 생성
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                gender TEXT)''')

# 몇 명의 사용자 추가
users = [
    ('John Doe', 25, 'Male'),
    ('Jane Smith', 30, 'Female'),
    ('Michael Johnson', 35, 'Male'),
    ('Emily Davis', 28, 'Female'),
    ('David Lee', 32, 'Male'),
    ('Emma Wilson', 27, 'Female'),
    ('Daniel Brown', 31, 'Male'),
    ('Olivia Taylor', 29, 'Female'),
    ('Sophia Anderson', 33, 'Female'),
    ('Matthew Martin', 26, 'Male')
]

# cursor.executemany('INSERT INTO users (name, age, gender) VALUES (?, ?, ?)', users)

# 변경사항 저장
conn.commit()

# 미션1 : 성별이 여자인 사람만 출력한다
result1 = cursor.execute("SELECT * FROM users WHERE gender='Female'")
result1 = cursor.fetchall() 
for r in result1:
    print(r)

# 미션2 : 나이가 30살 이상인 사람만 출력한다
result2 = cursor.execute("SELECT * FROM users WHERE age >= 30")
result2 = cursor.fetchall() 
print("---------------")
print("30살 이상인 사람:")
for r in result2:
    print(r)

# 미션3 : 나이가 25세 이상 30세 이하인 사용자를 출력한다
result3 = cursor.execute("SELECT * FROM users WHERE age BETWEEN 25 AND 30")
result3 = cursor.fetchall() 
print("---------------")
print("25세 이상 30세 이하인 사람:")
for r in result3:
    print(r)

# 미션4 : 성별로 그룹핑(남/여 각각) 몇 명인지 출력한다
cursor.execute("SELECT gender, COUNT(*) FROM users GROUP BY gender")
result4 = cursor.fetchall() 
print("---------------")
for gender, count in result4:
    print(f"{gender} : {count}")

# 미션5 : John Doe의 나이를 25살 -> 26살로 업데이트
cursor.execute("UPDATE users SET age=26 WHERE name='John Doe'")
conn.commit()

cursor.execute("SELECT * FROM users WHERE name='John Doe'")
result = cursor.fetchall()
print(result)

# 미션6 : Emily Davis 사용자를 삭제하시오
cursor.execute("DELETE FROM users WHERE name='Emily Davis'")
conn.commit()

cursor.execute("SELECT * FROM users WHERE name='Emily Davis'")
result = cursor.fetchall()
print(result)