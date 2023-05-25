
from source.player import Player
from source.personality import Personality
from source.enemy import Enemy
from source.battle import Battle
from source.inventory import Inventory
from data.api import Api


def roll_dice():
    print()
    input("Вы кидаете кости...\n")


Api().ROLL_DICE_FUNCTION = roll_dice

player = Player(Personality("Таранис", 9, 16, 9, 2), Inventory())
enemy = Enemy(Personality("Жаба", 6, 5, 0, 2))
battle = Battle(player, enemy)
battle.start()

