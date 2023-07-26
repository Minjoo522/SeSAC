from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.instance_path = os.getcwd()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crm.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.debug = True

db = SQLAlchemy(app)

class User(db.Model):
    # 클래스명과 테이블명이 1:1 매칭 되는 경우 자동으로 인식되지만, 매칭 안되는 경우 tablename 지정
    __tablename__ = 'user'
    # 컬럼 셋업
    id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(16))
    gender = db.Column(db.String(16))
    age = db.Column(db.Integer())
    birthdate = db.Column(db.String(32))
    address = db.Column(db.String(64))
    # 관계(relation) 셋업
    orderR = db.relationship('Order', backref='user')

    # 선택사항 : 없어도 문제 없음(그냥 print를 편하게 도와주는)
    def __repr__(self):
        return f'<User {self.name}, {self.gender}, {self.age}>'
    
class Store(db.Model):
    __tablename__ = 'store'
    id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(32))
    type = db.Column(db.String(32))
    address = db.Column(db.String(64))
    # 관계(relation) 셋업
    orderR = db.relationship('Order', backref='store')

    def __repr__(self):
        return f'<Store {self.name}, {self.type}>'
    
class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.String(64), primary_key=True)
    orderat = db.Column(db.String(64))
    storeid = db.Column(db.String(64), db.ForeignKey('store.id'))
    userid = db.Column(db.String(64), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Order {self.id}, {self.orderat}>'

@app.route('/')
def home():
    # users = User.query.filter_by(name="강은지").all()
    # print(users)
    # stores = Store.query.all()
    # print(stores)
    # for s in stores:
    #     print(s.address)
    # orders = Order.query.all()
    # print(orders)
    # users = User.query.filter_by(name="윤수빈").first()
    # order_by_user = users.orderR
    # print(order_by_user)

    # 윤수빈이 방문한 상점 명들을 출력하시오
    result = db.session.query(Store.name)\
                        .join(Order, Store.id == Order.storeid)\
                        .join(User, User.id == Order.userid)\
                        .filter(User.name == "윤수빈")\
                        .all()
    print(result)

    users = User.query.filter_by(name="윤수빈").first()
    # 윤수빈이 주문한 주문 내역
    order_by_user = users.orderR
    for order in order_by_user:
        store = order.store
        print(store.name)

    return "Hello"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(port=8080)