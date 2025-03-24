from abc import ABC, abstractmethod


class BaseRepository(ABC):

    @abstractmethod
    def get(self, id_: int):
        pass

