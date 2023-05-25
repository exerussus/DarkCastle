

class Personality:

    def __init__(self, name: str, dexterity: int, strength: int, charisma: int, attack_damage: int):
        self._name = name
        self._dexterity = dexterity
        self._strength = strength
        self._charisma = charisma
        self._current_strength = self._strength
        self._current_dexterity = self._dexterity
        self._attack_damage = attack_damage
        self._is_alive = True

    @property
    def name(self):
        return self._name

    @property
    def dexterity(self):
        return self._dexterity

    @property
    def strength(self):
        return self._strength

    @property
    def charisma(self):
        return self._charisma

    @property
    def current_strength(self):
        return self._current_strength

    @property
    def current_dexterity(self):
        return self._current_dexterity

    @property
    def current_charisma(self):
        return self._current_charisma

    @property
    def is_alive(self):
        return self._is_alive

    @property
    def attack_damage(self):
        return self._attack_damage

    @attack_damage.setter
    def attack_damage(self, damage_value):
        if damage_value > 0:
            self._attack_damage = damage_value

    def take_damage(self, hit_points: int) -> None:
        if hit_points > 0:
            self._current_strength -= hit_points
            if self._current_strength <= 0:
                self._is_alive = False

    def heal(self, hit_points: int) -> None:
        if hit_points > 0:
            self._current_strength += hit_points

