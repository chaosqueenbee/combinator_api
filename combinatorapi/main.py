from fastapi import FastAPI

from helper.schemas.article import Article
import helper

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/article/")
async def get_article() -> Article:
    return helper.article.get_top_article()


@app.get("/articles/{count}/")
async def get_articles(
    count: int
):
    return helper.article.get_top_articles(count=count)

def start():
  """Launched with `poetry run start` at root level"""
  uvicorn.run("combinatorapi.main:app", host="0.0.0.0", port=8000, reload=True)