import os
from flask import Flask, render_template
from database.db_controller import DbController
from datetime import date

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    db = DbController()
    db.connect_to_row()
    today = date.today()
    sql = f'SELECT * FROM movies WHERE create_at LIKE "%{today}%"'
    db.execute_query(sql)
    movies = db.fetch_all()
    db.close_connection()
    return render_template('index.html', today=today, movies=movies)

if __name__ == "__main__":
    app.run(debug=True, port=8008)

