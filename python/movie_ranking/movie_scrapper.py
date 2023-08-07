import requests
from bs4 import BeautifulSoup
from database.db_controller import DbController
from datetime import datetime

db = DbController()

db.connect()

data = requests.get('https://movie.daum.net/ranking/reservation')
soup = BeautifulSoup(data.text, 'html.parser')

movie_infos = soup.select('.item_poster')

for i, movie_info in enumerate(movie_infos):
    movie_url = 'https://movie.daum.net/'

    title = movie_info.select_one('.link_txt').text
    grade = float(movie_info.select_one('.txt_grade').text)
    number = float(movie_info.select_one('.txt_num').text[:-1])

    link = movie_url + movie_info.select_one('.link_story')['href'] 
    story = movie_info.select_one('.link_story').text.strip()

    movie = (i+1, title, grade, number, link, story, datetime.now())

    sql = 'INSERT INTO movies(ranking, title, grade, sales_rate, link, summary, create_at) VALUES(?, ?, ?, ?, ?, ?, ?)'
    db.execute_query(sql, movie)
    db.fetch_all()
    db.commit()

db.close_connection()

