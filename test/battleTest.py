
from source.player import Player
from source.personality import Personality
from source.enemy import Enemy
from source.battle import Battle
from source.inventory import Inventory


player = Player(Personality("Таранис", 9, 10, 9, 2), Inventory())
enemy1 = Enemy(Personality("Жаба", 6, 5, 0, 2))
enemy2 = Enemy(Personality("Лягуха", 7, 4, 0, 2))
enemy3 = Enemy(Personality("Болотная крыса", 10, 4, 0, 1))
battle = Battle(player, enemy1, enemy2, enemy3)
battle_result = battle.start()

if battle_result:
    print("You won!")
else:
    print("You lose!")
