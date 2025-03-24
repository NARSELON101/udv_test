import copy
import json
import pathlib
from typing import Union, List

from src.app.repository.base_repository import BaseRepository
from src.app.repository.models import Comment, News


class LocalJSONRepository(BaseRepository):
    def __init__(self):
        self.comments = []
        self.news = {}
        path = pathlib.Path(__file__).parent.resolve()
        with open(f'{path}/storage/news.json', 'r') as news:
            results = json.load(news)
            for news_ in results.get("news"):
                self.news.update({news_.get('id'): News(**news_)})

        with open(f'{path}/storage/comments.json', 'r') as comments:
            results = json.load(comments)
            for comment in results.get("comments"):
                record = Comment(**comment)
                if self._comment_in_news_id(record.news_id):
                    self.comments.append(record)

    def _comment_in_news_id(self, id_: int) -> bool:
        for news_ in self.news.values():
            if news_.id == id_:
                return True

        return False

    async def get(self, id_: int = None) -> Union[News, List[News]]:
        result = copy.deepcopy(self.news)
        for comment in self.comments:
            news = result.get(comment.news_id)
            if news:
                news.comments_count += 1
                news.comments.append(comment)
        if id_:
            return result.get(id_, None)
        else:
            return list(result.values())
