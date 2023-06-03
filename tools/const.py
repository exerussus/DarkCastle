

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
    HEALING = "++"
    DEXTERITY = ";;"


class SpellKeys:
    NAME = "name"
    DESCRIPTION = "description"
    KEYWORD = "keyword"


class ConstSpell:
    spellKeys = _sk = SpellKeys
    FIREBALL = {_sk.NAME: "Огненный шар", _sk.DESCRIPTION: "Огненный шар", _sk.KEYWORD: ConstKeyword.FIREBALL}
    COPY = {_sk.NAME: "Копия", _sk.DESCRIPTION: "Заклинание копии", _sk.KEYWORD: ConstKeyword.COPY}
    SWIMMING = {_sk.NAME: "Плавание", _sk.DESCRIPTION: "Заклинание плавания", _sk.KEYWORD: ConstKeyword.SWIMMING}
    LEVITATION = {_sk.NAME: "Левитация", _sk.DESCRIPTION: "Заклинание левитации", _sk.KEYWORD: ConstKeyword.LEVITATION}
    HEALING = {_sk.NAME: "Лечение", _sk.DESCRIPTION: "Заклинание лечения", _sk.KEYWORD: ConstKeyword.HEALING}
    DEXTERITY = {_sk.NAME: "Ловкость", _sk.DESCRIPTION: "Заклинание ловкости", _sk.KEYWORD: ConstKeyword.DEXTERITY}


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
    Spell = ConstSpell
