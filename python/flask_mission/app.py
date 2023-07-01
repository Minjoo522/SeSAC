from flask import Flask, render_template, request, redirect, url_for, session
import csv

app = Flask(__name__)
app.secret_key = 'hello'

def load_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data_list = []
        datas = csv.DictReader(file, skipinitialspace=True)
        for data in datas:
            data_list.append(data)
    return data_list

@app.route('/')
def index():
    if 'id' in session:
        return redirect(url_for('users'))
    else:
        return redirect(url_for('login'))

# Log in
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        id_ = request.form['id']
        password_ = request.form['password']
        if id_ != 'admin' or password_ != 'admin':
            error = '아이디나 비밀번호가 틀렸습니다.'
        else:
            session['id'] = id_
            return redirect(url_for('users'))
    return render_template("index.html", error = error)

# Log out
@app.route('/logout')
def logout():
    session.pop('id', None)

@app.route('/users')
def users():
    page = request.args.get('page', default=1, type=int)
    search_name = request.args.get('name', default="", type=str)
    search_gender = request.args.get('gender', default="", type=str)

    per_page = 10
    page_data = []
    data = []
    users = load_file("src/user.csv")

    for user in users:
        if search_name in user['Name']:
            if search_gender in user['Gender']:
                data.append(user)
    
    keywords = ""
    keywords += "&name=" + search_name
    keywords += "&gender=" + search_gender

    # TODO: 함수로 변경하기
    total_pages = len(data) // per_page + (len(data) % per_page > 0)
    start_index = per_page * (page - 1)
    end_index = start_index + per_page
    page_data = data[start_index:end_index]
    
    return render_template("users.html", users = page_data, total_pages = total_pages, current_page = page, keywords = keywords)

@app.route('/user_detail/<selected_id>')
def user_detail(selected_id):
    users = load_file("src/user.csv")
    for user in users:
        if user['Id'] == selected_id:
            return render_template("user_detail.html", user = user)

@app.route('/stores')
def stores():
    stores = load_file("src/store.csv")
    return render_template("stores.html", stores = stores)

@app.route('/store_detail/<selected_id>')
def store_detail(selected_id):
    stores = load_file("src/store.csv")
    for store in stores:
        if store['Id'] == selected_id:
            return render_template("store_detail.html", store = store)

@app.route('/items')
def items():
    items = load_file("src/item.csv")
    return render_template("items.html", items = items)
    
@app.route('/item_detail/<selected_id>')
def item_detail(selected_id):
    items = load_file("src/item.csv")
    for item in items:
        if item['Id'] == selected_id:
            return render_template("item_detail.html", item = item)
            
@app.route('/orders')
def orders():
    orders = load_file("src/order.csv")
    return render_template("orders.html", orders = orders)
    
# orderitem_detail
# @app.route('/orderitem_detail')

@app.route('/order_items')
def order_items():
    order_items = load_file("src/orderitem.csv")
    return render_template("order_items.html", order_items = order_items)

if __name__ == "__main__":
    app.run(debug=True, port=8001)