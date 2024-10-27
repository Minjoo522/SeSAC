import requests
from bs4 import BeautifulSoup
from database.db_controller import DbController
from datetime import date

db = DbController()

db.connect()

def movie_scraper():
    data = requests.get('https://movie.daum.net/ranking/reservation')
    soup = BeautifulSoup(data.text, 'html.parser')

    movie_infos = soup.select('.item_poster')

    # 1. 타이틀을 긁어온다
    for i, movie_info in enumerate(movie_infos):
        movie_url = 'https://movie.daum.net/'

    # 2. movies에 같은 이름을 가진 영화가 있는지 확인한다
        title = movie_info.select_one('.link_txt').text.strip()

        sql = f'SELECT id FROM movies WHERE title="{title}"'
        db.execute_query(sql)

    # 3. 없으면 정보를 추가해준다
        if not db.fetch_one():
            link = movie_url + movie_info.select_one('.link_story')['href'] 
            summary = movie_info.select_one('.link_story').text.strip()
            thumbnail_img = movie_info.select_one('.img_thumb')['src']

            # big img 구하기
            img_data = requests.get(link)
            img_soup = BeautifulSoup(img_data.text, 'html.parser')
            big_img = img_soup.select_one('meta[property="og:image"]')['content']

            sql = 'INSERT INTO movies(title, link, summary, thumbnail_img, big_img) VALUES(?, ?, ?, ?, ?)'
            db.execute_query(sql, (title, link, summary, thumbnail_img, big_img))
            db.commit()
    # 4. 영화 이름을 기준으로 찾아서 rankings에 넣어준다(movie_id(FK) = id(movies))
        rating = float(movie_info.select_one('.txt_grade').text)
        reservation_rate = float(movie_info.select_one('.txt_num').text.replace("%", ""))
        create_date = date.today()
        
        # movies의 id 찾기
        sql = f'SELECT id FROM movies WHERE title="{title}"'
        db.execute_query(sql)
        # 튜플로 받아와지기 때문에 인덱싱 함
        movie_id = db.fetch_one()[0]
        ranking = i + 1

        sql = f'INSERT INTO rankings(create_date, movie_id, ranking, rating, reservation_rate) VALUES(?, ?, ?, ?, ?)'
        db.execute_query(sql, (create_date, movie_id, ranking, rating, reservation_rate))
        db.commit()

# DB에 오늘 날짜인 정보가 있으면 업데이트 안하도록
today = date.today()
sql = 'SELECT * FROM rankings WHERE create_date = ? LIMIT 1'
db.execute_query(sql, (today, ))
if not db.fetch_one():
    movie_scraper()
db.close_connection()