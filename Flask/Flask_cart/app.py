from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'abcd1234' # 세션 암호화를 위한 나만의 키

# 상품 정보 등록
items = {
    'item1' : {'name': '상품1', 'price': 1000},
    'item2' : {'name': '상품2', 'price': 2000},
    'item3' : {'name': '상품3', 'price': 3000},
}

@app.route('/')
def index():
    return render_template('index.html', items = items)

@app.route('/add_to_cart/<item_name>')
def add_to_cart(item_name):
    if 'cart' not in session:
        session['cart'] = {}

    # 카트에 물건 담기
    if item_name in session['cart']:
        session['cart'][item_name] += 1
    else:
        session['cart'][item_name] = 1

    # 세션 데이터가 수정 되었음을 Flask에 알립니다
    session.modified = True

    # 담은 이후 액션
    return redirect(url_for('index'))

# index.html 페이지에서, 상품명을 클릭해서 이 URI가 호출되도록 구현하시오
# 장바구니 보기 버튼(링크)
# 장바구니 내용 세션을 통해 가져와서 cart.html에 출력

@app.route('/view_cart')
def view_cart():
    selected_items = []
    total_price = 0
    session_item = session.get('cart')

    for item_name, quantity in session_item.items():
        for item in items.values():
            if item['name'] == item_name:
                selected_item = {'name': item['name'], 'quantity': quantity, 'price': item['price']*quantity}
                selected_items.append(selected_item)
                total_price += selected_item['price']
    return render_template('cart.html', selected_items = selected_items, total_price = total_price)

@app.route('/remove_item_from_cart/<item_name>')
def remove_item_from_cart(item_name):
    session['cart'].pop(item_name)
    session.modified = True

    return redirect(url_for('view_cart'))


if __name__ == "__main__":
    app.run(host="0.0.0.0")