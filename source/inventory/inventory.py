from source.inventory.bag import Bag
from source.inventory.flask import Flask
from source.inventory.gold import Gold


class Inventory:

    def __init__(self):
        self._bag = Bag()
        self._gold = Gold()
        self._flask = Flask()

    @property
    def flask(self) -> Flask:
        return self._flask

    @property
    def gold(self) -> Gold:
        return self._gold

    @property
    def bag(self) -> Bag:
        return self._bag
