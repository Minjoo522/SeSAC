from flask import Flask, render_template, redirect, request
from database import Database

app = Flask(__name__)
db = Database()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create", methods=["POST"])
def create():
    title = request.form['title']
    message = request.form['message']

    # 데이터 저장
    sql = "INSERT INTO board(title, message) VALUES('{}', '{}')".format(title, message)
    db.execute(sql)
    db.commit()

    return "OK"

@app.route("/list")
def list():
    sql = "SELECT * FROM board"
    values = db.execute_fetch(sql)
    # json 형태로 key, value pair로 잘~ 만들어 준다... dict(), zip()
    keys = ["id", "title", "message"]
    dict_list = [dict(zip(keys, value)) for value in values]
    # for value in values:
    #   dict_list.append(dict(zip(keys, value)))
    
    return dict_list

@app.route("/update", methods=['POST'])
def update():
    id = request.form['id']
    new_title = request.form['title']
    new_message = request.form['message']
    sql = f"UPDATE board SET title=?, message=? WHERE id={id}"
    db.execute(sql, (new_title, new_message))
    db.commit()

    return "OK"

@app.route("/delete", methods=['POST'])
def delete():
    id = request.form['id']
    sql = "DELETE FROM board WHERE id=?"
    db.execute(sql, (id, ))
    db.commit()

    return "OK"

if __name__ == "__main__":
    app.run(debug=True, port=8080)