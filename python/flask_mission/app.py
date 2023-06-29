from flask import Flask, render_template, request
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

@app.route('/')

# @app.route('/users/<int:page>')
@app.route('/users')
def users():
    # get 방식
    page = request.args.get('page', default=1, type=int)
    search_name = request.args.get('name', default="", type=str)

    # 한 페이지 당 보여줄 컨텐츠 개수
    per_page = 10
    data = []
    page_data = []
    with open("src/user.csv", "r", encoding="utf-8") as file:
        users = csv.DictReader(file, skipinitialspace=True)
        for user in users:
            if search_name in user['Name']:
                data.append(user)
        
        headers = [header.strip() for header in users.fieldnames]
        # skipinitialspace=True : csv 파일 공백 처리
        # .fildnames 필드 네임(헤더)만 불러오기

        # 전체 페이지 구하기
        pages = len(data) / per_page
        if pages % per_page > 0:
            pages += 1
        total_pages = int(pages)
        
        start_index = per_page * (page - 1)
        end_index = start_index + per_page

        page_data = data[start_index:end_index]

        # Page Bar 처리
        
        return render_template("index.html", users = page_data, headers = headers, total_pages = total_pages, current_page = page)
        # 인자 여러개 보내줄 수 있음

@app.route('/user_detail/<selected_id>')
def user_detail(selected_id):
    with open ("src/user.csv", "r", encoding="utf-8") as file:
        users = csv.DictReader(file)
        for user in users:
            if user['Id'] == selected_id:
                return render_template("user_detail.html", user = user)
            
@app.route('/stores')
def stores():
    with open("src/store.csv", "r", encoding="utf-8") as file:
        stores = csv.DictReader(file)
        return render_template("stores.html", stores = stores)
    
@app.route('/store_detail/<selected_id>')
def store_detail(selected_id):
    with open("src/store.csv", "r", encoding="utf-8") as file:
        stores = csv.DictReader(file)
        for store in stores:
            if store['Id'] == selected_id:
                return render_template("store_detail.html", store = store)

@app.route('/items')
def items():
    with open("src/item.csv", "r", encoding="utf-8") as file:
        items = csv.DictReader(file)
        return render_template("items.html", items = items)
    
@app.route('/item_detail/<selected_id>')
def item_detail(selected_id):
    with open("src/item.csv", "r", encoding="utf-8") as file:
        items = csv.DictReader(file)
        for item in items:
            if item['Id'] == selected_id:
                return render_template("item_detail.html", item = item)
            
@app.route('/orders')
def orders():
    with open("src/order.csv", "r", encoding="utf-8") as file:
        orders = csv.DictReader(file)
        return render_template("orders.html", orders = orders)
    
# orderitem_detail

@app.route('/order_items')
def order_items():
    with open("src/orderitem.csv", "r") as file:
        order_items = csv.DictReader(file)
        return render_template("order_items.html", order_items = order_items)

if __name__ == "__main__":
    app.run(debug=True, port=8001)