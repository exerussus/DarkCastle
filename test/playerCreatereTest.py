from source.mechanics.playerCreator import PlayerCreator

player = PlayerCreator.make_new_player()

print(f"{player.character.name=}")
print(f"{player.character.dexterity=}")
print(f"{player.character.current_strength=}")
print(f"{player.character.charisma=}")

