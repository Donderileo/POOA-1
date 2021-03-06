from .crawler import Crawler
import requests
from bs4 import BeautifulSoup


class FolhaCrawler(Crawler):

    def __init__(self):
        self.nome = 'Folha de São Paulo'
        self.url = 'https://www.folha.uol.com.br/'

    def get_data(self):
        html_text = requests.get(self.url).content
        soup = BeautifulSoup(html_text, 'html.parser')
        data = []
            
        crawled = soup.find_all('a', class_='c-main-headline__url')
        crawled = crawled + soup.find_all('a', class_='c-headline__url')
        
        for c in crawled:
            url = c['href']
            title = c.find('h2')
            if title is not None:
                url = url.strip()
                title = title.get_text()
                title = title.strip()
                data.append((title,url))            

        return data