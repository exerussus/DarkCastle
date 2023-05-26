from data.apiConfig import ROLL_DICE_FUNCTION, NEXT_BUTTON_FUNCTION, INPUT_FUNCTION, OUTPUT_FUNCTION

class Api(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = ApiSettings()
        return cls.instance


class ApiSettings:
    def __init__(self):
        self.next_button = NEXT_BUTTON_FUNCTION
        self.input = INPUT_FUNCTION
        self.output = OUTPUT_FUNCTION
        self.roll_dice = ROLL_DICE_FUNCTION

        self.roll_dice = self.roll_dice if self.roll_dice is not None else input
        self.next_button = self.next_button if self.next_button is not None else input
        self.input = self.input if self.input is not None else input
        self.output = self.output if self.output is not None else print
