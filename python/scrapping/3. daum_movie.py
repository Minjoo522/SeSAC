import requests
from bs4 import BeautifulSoup

data = requests.get('https://movie.daum.net/ranking/reservation')
soup = BeautifulSoup(data.text, 'html.parser')

movie_infos = soup.select('.item_poster')
movie_ranking = []

for i, movie_info in enumerate(movie_infos):
    movie_url = 'https://movie.daum.net/'
    keys = ['순위', '제목', '평점', '예매율', '링크', '소개']

    title = movie_info.select_one('.link_txt').text
    grade = float(movie_info.select_one('.txt_grade').text)
    number = float(movie_info.select_one('.txt_num').text[:-1])

    link = movie_url + movie_info.select_one('.link_story')['href'] 
    story = movie_info.select_one('.link_story').text.strip()

    values = [i+1, title, grade, number, link, story]
    movie_ranking.append(dict(zip(keys, values)))

print(movie_ranking)