

class Api(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = ApiSettings()
        return cls.instance


class ApiSettings:
    def __init__(self):
        self.NEXT_BUTTON_FUNCTION = None
        self.INPUT_FUNCTION = None
        self.OUTPUT_FUNCTION = None
        self.ROLL_DICE_FUNCTION = None

        self.ROLL_DICE_FUNCTION = self.ROLL_DICE_FUNCTION if self.ROLL_DICE_FUNCTION is not None else input
        self.NEXT_BUTTON_FUNCTION = self.NEXT_BUTTON_FUNCTION if self.NEXT_BUTTON_FUNCTION is not None else input
        self.INPUT_FUNCTION = self.INPUT_FUNCTION if self.INPUT_FUNCTION is not None else input
        self.OUTPUT_FUNCTION = self.OUTPUT_FUNCTION if self.OUTPUT_FUNCTION is not None else print
