from source.playerCreator import PlayerCreator

player = PlayerCreator.make_new_player()

print(f"{player.name=}")
print(f"{player.dexterity=}")
print(f"{player.current_strength=}")
print(f"{player.charisma=}")

