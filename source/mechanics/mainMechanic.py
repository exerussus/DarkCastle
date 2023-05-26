
from source.mechanics.playerCreator import PlayerCreator
from tools.sqlOperator import SqlOperator
from tools.const import Const
from tools.parser import Parser


class MainMechanic:

    def __init__(self):
        self._player = PlayerCreator.make_new_player()
        self._history = SqlOperator()

    def start(self):
        pass
