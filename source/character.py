from source.personality import Personality


class Character:

    def __init__(self, personality: Personality):
        self._personality = personality

    def take_damage(self, damage: int):
        self._personality.take_damage(damage)

    def heal(self, hp: int):
        self._personality.heal(hp)

    def get_dexterity(self):
        return self._personality.current_dexterity

    @property
    def is_alive(self):
        return self._personality.is_alive

