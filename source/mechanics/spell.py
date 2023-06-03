
from abc import ABC, abstractmethod


class Spell(ABC):

    def __init__(self, keyword: str):
        self._keyword = keyword

    @abstractmethod
    def cast(self):
        pass

