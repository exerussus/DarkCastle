

class Gold:

    def __init__(self):
        self._value = 15

    def add_gold(self, value: int) -> None:
        if value > 0:
            self._value += value

    def get_is_gold_enough(self, cost_value: int) -> bool:
        return True if self._value >= cost_value else False

    def spend_gold(self, value: int) -> None:
        self._value -= value
        if self._value < 0:
            self._value = 0

