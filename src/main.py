from fastapi import FastAPI

from src.app.urls.urls import router as news

from src.app.repository.local_repository import LocalJSONRepository
from src.app.services.news_service import NewsService

app = FastAPI(title='Сервис новостей', version='1.0.0')


@app.on_event("startup")
async def init_db():
    db = LocalJSONRepository()
    app.news_service = NewsService(db=db)


app.include_router(news, prefix="/v1")
