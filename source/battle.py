from tools.api import Api
from source.player import Player
from source.dice import Dice
from source.enemy import Enemy


class Battle:

    def __init__(self, player: Player, *enemies: Enemy):
        self._player = player
        self._enemies = list(enemies)
        self._is_first_attack = True
        self._demoralize_value_damage = 2
        self._demoralize_value_parry = 1
        self._inspire_value_attack = 1

    def start(self) -> bool:
        return self._round()

    def _roll(self, character) -> int:
        roll = Dice.roll_d12(character.dexterity)
        Api().output(f"{character.name} выбрасывает: {roll}.")
        return roll

    def _reset_before_round(self):
        self._is_first_attack = True

    def _get_is_enemies_defeated(self):
        return True if len(self._enemies) == 0 else False

    def _clear_corps(self):
        count = len(self._enemies)
        while count > 0:
            count -= 1
            if self._enemies[count].current_strength <= 0:
                self._enemies.pop(count)

    def _attack_choose(self):
        Api().output(f"Кого следует атаковать?")
        enemies_count = 0
        for enemy in self._enemies:
            enemies_count += 1
            Api().output(f"{enemies_count}. {enemy.name} "
                         f"| Ловкость: {enemy.dexterity} "
                         f"| Здоровье: {enemy.current_strength}")
        Api().output(f"\n")
        try:
            choice = int(Api().input())
            if len(self._enemies) >= choice:
                target_index = choice - 1
                target = self._enemies[target_index]
                first_enemy = self._enemies[0]
                self._enemies[0] = target
                self._enemies[target_index] = first_enemy
        except:
            pass

    def _deal_damage(self, enemy: Enemy, player_roll: int, enemy_roll: int):
        if player_roll > enemy_roll:
            if self._is_first_attack:
                enemy.take_damage(self._player.attack_damage)
                enemy.demoralize(self._demoralize_value_damage)
                self._is_first_attack = False
                if enemy.is_alive:
                    Api().output(f"{enemy.name} получает урон! Его здоровье опустилось до: {enemy.current_strength}.")
                else:
                    Api().output(f"{enemy.name} получает урон и погибает!")
            else:
                enemy.demoralize(self._demoralize_value_parry)
                Api().output(f"{self._player.name} парирует атаку, которую наносит {enemy.name}.")
        elif player_roll < enemy_roll:
            self._player.take_damage(enemy.attack_damage)
            enemy.inspire(self._inspire_value_attack)
            if self._player.is_alive:
                Api().output(f"{self._player.name} получает урон! "
                               f"Его здоровье опустилось до: {self._player.current_strength}.")
            else:
                Api().output(f"{self._player.name} получает урон и погибает!")
        else:
            enemy.demoralize(self._demoralize_value_parry)
            Api().output(f"{self._player.name} парирует атаку, которую наносит {enemy.name}.")

    def _round(self):
        self._reset_before_round()
        self._attack_choose()
        player_roll = self._roll(self._player)
        for enemy in self._enemies:
            if enemy.is_alive:
                enemy_roll = self._roll(enemy)
                self._deal_damage(enemy=enemy, player_roll=player_roll, enemy_roll=enemy_roll)
        self._clear_corps()
        if not self._player.is_alive:
            return False
        elif self._get_is_enemies_defeated():
            return True
        else:
            return self._round()

