from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('crm.db', check_same_thread=False)
cursor = conn.cursor()

@app.route('/')
def index():
    # TODO: 월간 매출액 합산을 구하시오.
    # 테이블로 2023-1, ..., 2023-12까지 월간 매출액을 구하는 쿼리문 작성
    query = """
            SELECT SUBSTR(O.OrderAt, 6, 2) AS "ordermonth", SUM(I.UnitPrice) FROM item I
            JOIN orderitem OI
            ON I.Id = OI.ItemId
            JOIN orders O
            ON OI.OrderId = O.Id
            WHERE SUBSTR(O.OrderAt, 1, 4) = "2023"
            GROUP BY ordermonth
            """
    cursor.execute(query)
    rows = cursor.fetchall()

    labels = []
    revenues = []
    for row in rows:
        labels.append(row[0])
        revenues.append(row[1])

    return render_template("index.html", rows=rows, labels=labels, revenues=revenues)

if __name__ == "__main__":
    app.run(debug=True, port=8001)