from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route('/users')
def users():
    with open("src/user.csv", "r") as file:
        users = csv.DictReader(file)
        return render_template("index.html", users = users)
    
@app.route('/user_detail/<selected_id>')
def user_detail(selected_id):
    with open ("src/user.csv", "r") as file:
        users = csv.DictReader(file)
        for user in users:
            if user['Id'] == selected_id:
                return render_template("user_detail.html", user = user)
            
@app.route('/stores')
def stores():
    with open("src/store.csv", "r") as file:
        stores = csv.DictReader(file)
        return render_template("stores.html", stores = stores)
    
@app.route('/store_detail/<selected_id>')
def store_detail(selected_id):
    with open("src/store.csv", "r") as file:
        stores = csv.DictReader(file)
        for store in stores:
            if store['Id'] == selected_id:
                return render_template("store_detail.html", store = store)

@app.route('/items')
def items():
    with open("src/item.csv", "r") as file:
        items = csv.DictReader(file)
        return render_template("items.html", items = items)
    
@app.route('/item_detail/<selected_id>')
def item_detail(selected_id):
    with open("src/item.csv", "r") as file:
        items = csv.DictReader(file)
        for item in items:
            if item['Id'] == selected_id:
                return render_template("item_detail.html", item = item)
            
@app.route('/orders')
def orders():
    with open("src/order.csv", "r") as file:
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