

class Flask:

    def __init__(self):
        self._sip = 2

    @property
    def flask_sip_count(self):
        return self._sip

    def _get_is_enough_to_drink(self):
        return True if self._sip > 0 else False

    def _drink(self):
        self._sip -= 1
        if self._sip < 0:
            self._sip = 0

    def fill(self):
        self._sip = 2

    def get_drink_if_enough(self) -> bool:
        if self._get_is_enough_to_drink():
            self._drink()
            return True
        else:
            return False
