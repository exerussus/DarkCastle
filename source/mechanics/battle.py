from tools.api import Api
from source.character.player import Player
from tools.dice import Dice
from source.character.enemy import Enemy


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

    def _roll(self, dexterity: int, character_name: str) -> int:
        roll = Dice.roll_d12(dexterity)
        Api().output(f"{character_name} выбрасывает: {roll}.")
        return roll

    def _reset_before_round(self):
        self._is_first_attack = True

    def _get_is_enemies_defeated(self):
        return True if len(self._enemies) == 0 else False

    def _clear_corps(self):
        count = len(self._enemies)
        while count > 0:
            count -= 1
            if self._enemies[count].character.current_strength <= 0:
                self._enemies.pop(count)

    def _attack_choose(self):
        Api().output(f"Кого следует атаковать?")
        enemies_count = 0
        for enemy in self._enemies:
            enemies_count += 1
            Api().output(f"{enemies_count}. {enemy.character.name} "
                         f"| Ловкость: {enemy.character.dexterity} "
                         f"| Здоровье: {enemy.character.current_strength}")
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
                enemy.take_damage(self._player.character.attack_damage)
                enemy.demoralize(self._demoralize_value_damage)
                self._is_first_attack = False
                if enemy.character.is_alive:
                    Api().output(f"{enemy.character.name} получает урон! "
                                 f"Его здоровье опустилось до: {enemy.character.current_strength}.")
                else:
                    Api().output(f"{enemy.character.name} получает урон и погибает!")
            else:
                enemy.demoralize(self._demoralize_value_parry)
                Api().output(f"{self._player.character.name} парирует атаку, которую наносит {enemy.character.name}.")
        elif player_roll < enemy_roll:
            self._player.character.take_damage(enemy.attack_fixed_damage)
            enemy.inspire(self._inspire_value_attack)
            if self._player.character.is_alive:
                Api().output(f"{self._player.character.name} получает урон! "
                             f"Его здоровье опустилось до: {self._player.character.current_strength}.")
            else:
                Api().output(f"{self._player.character.name} получает урон и погибает!")
        else:
            enemy.demoralize(self._demoralize_value_parry)
            Api().output(f"{self._player.character.name} парирует атаку, которую наносит {enemy.character.name}.")

    def _round(self):
        self._reset_before_round()
        self._attack_choose()
        player_roll = self._roll(self._player.character.dexterity, self._player.character.name)
        for enemy in self._enemies:
            if enemy.character.is_alive:
                enemy_roll = self._roll(enemy.character.dexterity, enemy.character.name)
                self._deal_damage(enemy=enemy, player_roll=player_roll, enemy_roll=enemy_roll)
        self._clear_corps()
        if not self._player.character.is_alive:
            return False
        elif self._get_is_enemies_defeated():
            return True
        else:
            return self._round()

