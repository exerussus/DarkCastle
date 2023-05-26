

class Const:

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = Constant()
        return cls.instance


class ConstParam:
    DEXTERITY = "dexterity"
    STRENGTH = "strength"
    CHARISMA = "charisma"

    DEXTERITY_NAME = "ловкость"
    STRENGTH_NAME = "сила"
    CHARISMA_NAME = "харизма"


class ConstKeyword:
    SEPARATOR = "|"
    COPY = "**"
    FIREBALL = "@@"
    SWIMMING = "%%"
    LEVITATION = "^^"
    FIGHT = "##"
    CHECK = "$$"
    NEXT = "0"


class ConstTableName:
    TEXT = 'text'
    TRANSITION = 'transition'
    ITEM = 'item'
    ENEMY = 'enemy'
    CHECK = 'check'


class Constant:
    Parameter = ConstParam
    Keyword = ConstKeyword
    TableName = ConstTableName
