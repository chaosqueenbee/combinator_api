from fastapi import FastAPI

from helper.schemas.article import Article
import helper

app = FastAPI()


@app.get("/article/")
async def get_article() -> Article:
    return helper.article.get_top_article()

@app.get("/articles/{count}/")
async def get_articles(
    count: int
):
    return helper.article.get_top_articles(count=count)