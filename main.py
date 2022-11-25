import requests
import bs4

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

base_url = 'https://habr.com'
url = base_url + '/ru/all/'



response = requests.get(url)
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')
for article in articles:
    hubs = article.find_all(class_='tm-article-snippet tm-article-snippet')
    hubs = [hub.text.strip() for hub in hubs]
    for hub in hubs:
        if hub in KEYWORDS:
            title = article.find('h2').find('span').text
            href = article.find(class_='tm-article-snippet__title-link').attrs['href']
            link = base_url + href
            data = article.find(class_='tm-article-snippet__datetime-published').text
            print(f'дата - {data}, заголовок - {title}, ссылка - {link}')
