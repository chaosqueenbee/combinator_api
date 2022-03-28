from .web_scraper import WebScraper

class Combinator:
    def __init__(self):
        web_scraper = WebScraper()

        combinator_page = web_scraper.get_page('https://news.ycombinator.com/best')
        
        if combinator_page.status_code != 200:
            raise ValueError("Error retrieving page.")
        
        self.combinator_html = web_scraper.scrape(combinator_page.content)
        
    def get_top_links(self, count):
        links = self.combinator_html.find_all(class_='titlelink')
        return links[0:count]
    
    def get_element_title(self, element):
        return element.get_text()
    
    def get_element_link(self, element):
        return element['href']