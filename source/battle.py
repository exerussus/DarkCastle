from data.api import Api
from source.player import Player
from source.dice import Dice
from source.enemy import Enemy


class Battle:

    _next_button = Api.NEXT_BUTTON_FUNCTION
    _roll_dice = Api.ROLL_DICE_FUNCTION
    _input = Api.INPUT_FUNCTION
    _output = Api.OUTPUT_FUNCTION

    def __init__(self, player: Player, *enemies: Enemy):
        self._player = player
        self._enemies = enemies
        self._is_first_attack = True
        self._demoralize_value_damage = 2
        self._demoralize_value_parry = 1
        self._inspire_value_attack = 1

    def start(self) -> bool:
        return self.round()

    def roll(self, character) -> int:
        roll = Dice.roll_d12(character.dexterity)
        Battle._output(f"{character.name} выбрасывает: {roll}.")
        return roll

    def reset_before_round(self):
        self._is_first_attack = True

    def get_is_enemies_defeated(self):
        is_defeated = True
        for enemy in self._enemies:
            if enemy.is_alive:
                is_defeated = False
        return is_defeated

    def deal_damage(self, enemy: Enemy, player_roll: int, enemy_roll: int):
        if player_roll > enemy_roll:
            if self._is_first_attack:
                enemy.take_damage(self._player.attack_damage)
                enemy.demoralize(self._demoralize_value_damage)
                self._is_first_attack = False
                if enemy.is_alive:
                    Battle._output(f"{enemy.name} получает урон! Его здоровье опустилось до: {enemy.current_strength}.")
                else:
                    Battle._output(f"{enemy.name} получает урон и погибает!")
            else:
                enemy.demoralize(self._demoralize_value_parry)
                Battle._output(f"{self._player.name} парирует атаку, которую наносит {enemy.name}.")
        elif player_roll < enemy_roll:
            self._player.take_damage(enemy.attack_damage)
            enemy.inspire(self._inspire_value_attack)
            if self._player.is_alive:
                Battle._output(f"{self._player.name} получает урон! "
                               f"Его здоровье опустилось до: {self._player.current_strength}.")
            else:
                Battle._output(f"{self._player.name} получает урон и погибает!")
        else:
            enemy.demoralize(self._demoralize_value_parry)
            Battle._output(f"{self._player.name} парирует атаку, которую наносит {enemy.name}.")

    def round(self):
        self.reset_before_round()
        Battle._roll_dice()
        player_roll = self.roll(self._player)
        for enemy in self._enemies:
            if enemy.is_alive:
                enemy_roll = self.roll(enemy)
                self.deal_damage(enemy=enemy, player_roll=player_roll, enemy_roll=enemy_roll)
        if not self._player.is_alive:
            return False
        elif self.get_is_enemies_defeated():
            return True
        else:
            return self.round()

