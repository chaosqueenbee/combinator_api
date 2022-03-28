from .web_scraper.combinator import Combinator
from .schemas.article import Article

def get_top_article() -> Article:
    articles = get_top_articles(count=1)
    return articles[0] if articles else []

def get_top_articles(
    count: int,
) -> [Article]:
    combinator = Combinator()
    links = combinator.get_top_links(count)

    articles = []
    for link in links:
        article = Article(
            title=combinator.get_element_title(link),
            url=combinator.get_element_link(link)
        )
        articles.append(article)
    
    return articles
