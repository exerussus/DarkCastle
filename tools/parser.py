
from tools.const import Const


class Parser:

    @staticmethod
    def parse_location(location_info: dict) -> dict:
        location_dict: dict = {}

        text_raw: str = location_info[Const().TableName.TEXT]
        transition_raw: str = location_info[Const().TableName.TRANSITION]
        item_raw: str = location_info[Const().TableName.ITEM]
        enemy_raw: str = location_info[Const().TableName.ENEMY]
        check_raw: str = location_info[Const().TableName.CHECK]

        text: list = Parser._parse_text(text_raw)
        transition: dict = Parser._parse_transition(transition_raw)

        location_dict[Const().TableName.TEXT] = text
        location_dict[Const().TableName.TRANSITION] = transition

        return location_dict

    @staticmethod
    def _parse_text(text: str) -> list:
        return text.split(Const().Keyword.SEPARATOR)

    @staticmethod
    def _parse_transition(transition: str):
        transition_dict: dict = {}

        if transition[0] == Const().Keyword.NEXT:
            transition_dict[1] = {Const().TableName.TRANSITION: int(transition[2:])}
            return transition_dict

        list_raw = transition.split(Const().Keyword.SEPARATOR)

        element_count = 0
        for element in list_raw:
            element_count += 1
            split_transition = element.split(",")
            transition_dict[element_count] = {
                Const().TableName.TEXT: split_transition[0],
                Const().TableName.TRANSITION: split_transition[1]
                                              }

        return transition_dict

    @staticmethod
    def _parse_item():
        pass

    @staticmethod
    def _parse_enemy():
        pass

    @staticmethod
    def _parse_check():
        pass

