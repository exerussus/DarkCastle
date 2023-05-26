

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


class ConstSpell:
    copy = "**"
    fireball = "@@"
    swimming = "%%"
    levitation = "^^"


class Constant:
    Parameter = ConstParam
    Spell = ConstSpell
