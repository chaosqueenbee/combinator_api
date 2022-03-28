import requests

from bs4 import BeautifulSoup

class WebScraper:
    def get_page(self, url):
        return requests.get(url)

    def scrape(self, content):
        return BeautifulSoup(content, 'html.parser')