import requests
from bs4 import BeautifulSoup

def get_naver_sportsnews():
    data = requests.get('https://sports.naver.com/index')
    soup = BeautifulSoup(data.text, 'html.parser')

    naver_news_url = 'https://sports.naver.com'

    news = soup.select('.today_list > li')

    # 방법 1
    titles = []
    for n in news:
        # 타이틀 제목을 가져온다
        title = n.select_one('.title').text.strip()
        titles.append(title)

    # 방법 2
    for n in news:
        a_tag = n.select_one('a')
        print('🚨 ', a_tag['title'])
        news_url = naver_news_url+a_tag['href']
        print_news_content(news_url)
        print(news_url)

def print_news_content(url):
    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'html.parser')
    news_content = soup.select_one('.news_end')
    if news_content:
        start_span = news_content.find('span')
        end_p = news_content.find('p', class_='source')
        if start_span and end_p:
            content = start_span.next_element
            while content and content != end_p:
                if isinstance(content, str) and content.strip():
                    print(content.strip())
                content = content.next_element
    print('*' * 150)

def get_naver_land(type):
    data = requests.get('https://land.naver.com/news/')
    soup = BeautifulSoup(data.text, 'html.parser')
    if type == 'headline':
        # 분야별 헤드라인 정보 가져오기
        headlines_warp = soup.select_one('.list_type')
        headlines = headlines_warp.select('li')

        naver_land_url = 'https://land.naver.com/'
        links = []

        for headline in headlines:
            title = headline.select('a')
            print(title[0].text, title[1].text)

            # 헤드라인 기사의 본문 내용중 text 부분을 다 가져온다.
            link = title[1]['href']
            links.append(naver_land_url+link)
            
        for link in links:
            link_data = requests.get(link)
            link_soup = BeautifulSoup(link_data.text, 'html.parser')

            title = link_soup.select_one('.article_header > h3').text
            content = link_soup.select_one('#articleBody').text
            print(title)
            print(content)
            print('---------------------------------')

    elif type == 'trend':
        # 동향보고서 내용 가져오기
        reports1 = soup.select('.h_report + .list_type > li')
        reports2 = soup.select('.h_report + .list_type + .list_type > li')
        # 전달
        for report in reports1:
            report_title = report.select_one('a').text.strip()
            print(report_title)
        # 전전달
        for report in reports2:
            report_title = report.select_one('a').text.strip()
            print(report_title)
    
    else:
        print('Unkown type')

if __name__ == "__main__":
    get_naver_sportsnews()
    # get_naver_land('headline')