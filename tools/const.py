

class Const:

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = ConstParams()
        return cls.instance


class ConstParams:
    DEXTERITY = "dexterity"
    STRENGTH = "strength"
    CHARISMA = "charisma"

    DEXTERITY_NAME = "ловкость"
    STRENGTH_NAME = "сила"
    CHARISMA_NAME = "харизма"

