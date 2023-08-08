import requests
from bs4 import BeautifulSoup
from database.db_controller import DbController
from datetime import date

db = DbController()

db.connect()

data = requests.get('https://movie.daum.net/ranking/reservation')
soup = BeautifulSoup(data.text, 'html.parser')

movie_infos = soup.select('.item_poster')

# 1. 타이틀을 긁어온다(순위는 순서대로)
for i, movie_info in enumerate(movie_infos):
    movie_url = 'https://movie.daum.net/'

# 2. movies에 같은 이름을 가진 영화가 있는지 확인한다
    title = movie_info.select_one('.link_txt').text.strip()

    sql = f'SELECT id FROM movies WHERE title="{title}"'
    db.execute_query(sql)
    result = db.fetch_one()
    if not result:
# 3. 없으면 정보를 추가해준다
        link = movie_url + movie_info.select_one('.link_story')['href'] 
        summary = movie_info.select_one('.link_story').text.strip()

        sql = 'INSERT INTO movies(title, link, summary) VALUES(?, ?, ?)'
        db.execute_query(sql, (title, link, summary))
        db.commit()
# 4. 영화 이름을 기준으로 찾아서 rankings에 넣어준다(movie_id(FK) = id(movies))
    rating = float(movie_info.select_one('.txt_grade').text)
    reservation_rate = float(movie_info.select_one('.txt_num').text.replace("%", ""))
    create_at = date.today()
    
    # movies의 id 찾기
    sql = f'SELECT id FROM movies WHERE title="{title}"'
    db.execute_query(sql)
    movie_id = db.fetch_one()[0]
    ranking = i + 1

    sql = f'INSERT INTO rankings(create_date, movie_id, ranking, rating, reservation_rate) VALUES(?, ?, ?, ?, ?)'
    db.execute_query(sql, (create_at, movie_id, ranking, rating, reservation_rate))
    db.commit()

db.close_connection()