import random


class Dice:

    @staticmethod
    def roll_d6(additional_value=0) -> int:
        return random.randint(1, 6) + additional_value

    @staticmethod
    def roll_d12(additional_value=0) -> int:
        return random.randint(1, 12) + additional_value
