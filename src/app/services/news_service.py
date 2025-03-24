from src.app.repository.local_repository import LocalJSONRepository


class NewsServiceError(Exception):
    pass


class NewsService:
    """ Сервисный слой

        Выполняет основную логику приложения, так же взаимодействует с БД
    """

    def __init__(self, db: LocalJSONRepository):
        self.db = db

    async def get_single_news(self, id_: int):

        result = await self.db.get(id_=id_)

        if result:
            if result.deleted:
                raise NewsServiceError("Запись удалена")

            result = result.model_dump()

            return result
        raise NewsServiceError("Запись не найдена")

    async def get_all_news(self):
        final_result = dict()
        list_news = []
        result = await self.db.get()
        for news_ in result:
            news_ = news_.model_dump()
            news_.pop('comments')
            list_news.append(news_)

        final_result['news'] = list_news
        final_result['news_count'] = len(final_result['news'])
        print(final_result)
        return final_result
