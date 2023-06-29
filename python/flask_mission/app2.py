from flask import Flask, render_template
import csv

app = Flask(__name__)

# 페이징 처리
# 1. 총 데이터 수를 구한다
# 2. 보여줄 데이터 개수
# 3. 총 데이터 수 / 보여줄 데이터 개수 = 결과가 float이면 int로 바꾸고 + 1 -> 총 페이지 수

# 1. 한 페이지에 담길 컨텐츠 수를 정한다(num)
# 2. num에 갯수만큼 데이터를 잘라준다
# 3. 페이지에 이 데이터를 전달한다
# 4. 페이지를 구분하기 위한 인덱스(현재 페이지 준다)
# 5. 인덱스의 시작부터 끝가지의 숫자를 전달한다.

@app.route('/users/<int:page>')
def users(page=1):
    # 한 페이지 당 보여줄 컨텐츠 개수
    per_page = 10
    data = []
    page_data = []
    with open("src/user.csv", "r", encoding="utf-8") as file:
        users = csv.DictReader(file, skipinitialspace=True)
        for user in users:
            data.append(user)
        headers = [header.strip() for header in users.fieldnames]
        # skipinitialspace=True : csv 파일 공백 처리
        # .fildnames 필드 네임(헤더)만 불러오기

        # 전체 페이지 구하기
        total_pages = (len(data) // per_page) + 1
        start_index = per_page * (page - 1)
        end_index = start_index + per_page

        page_data = data[start_index:end_index]
        return render_template("index.html", users = page_data, headers = headers, total_pages = total_pages)
    
if __name__ == "__main__":
    app.run(debug=True, port=8001)