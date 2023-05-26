
from source.player import Player
from source.dice import Dice
from source.personality import Personality
from source.inventory import Inventory
from tools.api import Api
from tools.const import Const


class PlayerCreator:

    _DEXTERITY = Const().DEXTERITY
    _STRENGTH = Const().STRENGTH
    _CHARISMA = Const().CHARISMA

    _raw_params = {
        2: {_DEXTERITY: 8, _STRENGTH: 22, _CHARISMA: 8},
        3: {_DEXTERITY: 10, _STRENGTH: 20, _CHARISMA: 6},
        4: {_DEXTERITY: 12, _STRENGTH: 16, _CHARISMA: 5},
        5: {_DEXTERITY: 9, _STRENGTH: 18, _CHARISMA: 8},
        6: {_DEXTERITY: 11, _STRENGTH: 20, _CHARISMA: 6},
        7: {_DEXTERITY: 9, _STRENGTH: 20, _CHARISMA: 7},
        8: {_DEXTERITY: 10, _STRENGTH: 16, _CHARISMA: 7},
        9: {_DEXTERITY: 8, _STRENGTH: 24, _CHARISMA: 7},
        10: {_DEXTERITY: 9, _STRENGTH: 22, _CHARISMA: 6},
        11: {_DEXTERITY: 10, _STRENGTH: 18, _CHARISMA: 7},
        12: {_DEXTERITY: 11, _STRENGTH: 20, _CHARISMA: 5},

    }

    @staticmethod
    def make_new_player() -> Player:

        def roll_dice() -> int:
            return Dice.roll_d6() + Dice.roll_d6()

        def get_parameter(parameter: str, parameter_name_language: str) -> int:
            Api().output(f"Бросок на {parameter_name_language}: ")
            Api().roll_dice()
            raw_value = roll_dice()
            Api().output(f"Ваш бросок равен: {raw_value}")
            pure_value = PlayerCreator._raw_params[raw_value][parameter]
            Api().output(f"{parameter_name_language.title()} равна {pure_value}")
            return pure_value

        def get_character_name():
            Api().output("Назовите вашего персонажа: ")
            character_name = Api().input()
            max_letters = 20
            if len(character_name) > max_letters:
                character_name = character_name[:-(len(character_name) - max_letters)]
            return character_name

        name = get_character_name()
        dexterity = get_parameter(PlayerCreator._DEXTERITY, Const().DEXTERITY_NAME)
        strength = get_parameter(PlayerCreator._STRENGTH, Const().STRENGTH_NAME)
        charisma = get_parameter(PlayerCreator._CHARISMA, Const().CHARISMA_NAME)

        return Player(Personality(name, dexterity, strength, charisma, 2), Inventory())


