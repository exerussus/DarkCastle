
from source.character.player import Player
from source.character.character import Character
from source.character.enemy import Enemy
from source.mechanics.battle import Battle
from source.inventory.inventory import Inventory


player = Player(Character("Таранис", 9, 10, 9, 2), Inventory())
enemy1 = Enemy(Character("Жаба", 6, 5, 0, 2))
enemy2 = Enemy(Character("Лягуха", 7, 4, 0, 2))
enemy3 = Enemy(Character("Болотная крыса", 10, 4, 0, 1))
battle = Battle(player, enemy1, enemy2, enemy3)
battle_result = battle.start()

if battle_result:
    print("You won!")
else:
    print("You lose!")
