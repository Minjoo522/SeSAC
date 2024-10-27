import os
from flask import Flask, render_template
from database.db_controller import DbController

app = Flask(__name__)
app.secret_key = os.urandom(24)

db = DbController()

@app.route('/')
def index():
    db.connect()
    sql = 'SELECT DISTINCT create_date FROM rankings ORDER BY create_date DESC'
    db.execute_query(sql)
    dates = db.fetch_all()
    db.close_connection()
    return render_template('index.html', dates=dates)

@app.route('/ranking/<date>/')
def ranking(date):
    db.connect_to_row()
    sql = f'SELECT * FROM rankings R, movies M WHERE R.movie_id = M.id AND R.create_date LIKE "{date}"'
    db.execute_query(sql)
    movies = db.fetch_all()

    db.close_connection()
    return render_template('ranking.html', date=date, movies=movies)

if __name__ == "__main__":
    app.run(debug=True, port=8001)

