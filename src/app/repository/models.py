from pydantic import BaseModel


class News(BaseModel):
    """ Модель новости """
    id: int
    title: str
    date: str
    body: str
    deleted: bool
    comments: list = []
    comments_count: int = 0


class Comment(BaseModel):
    """ Модель комментария к новости """
    id: int
    news_id: int
    title: str
    date: str
    comment: str
