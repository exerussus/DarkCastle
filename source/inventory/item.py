

class Item:

    def __init__(self, name: str, transition_value: int):
        self._name = name
        self._transition_value = transition_value

    @property
    def name(self):
        return self._name

    @property
    def transition_value(self):
        return self._transition_value
