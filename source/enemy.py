from source.personality import Personality


class Enemy:

    def __init__(self, personality: Personality, morality: int = 0):
        self._personality = personality
        self._morality = morality
        self._can_be_afraid = True if self._morality != 0 else False
        self._is_afraid = True

    @property
    def name(self) -> bool:
        return self._personality.name

    @property
    def is_alive(self) -> bool:
        return self._personality.is_alive

    @property
    def is_afraid(self) -> bool:
        return self._is_afraid

    @property
    def attack_damage(self) -> int:
        return self._personality.attack_damage + 1 if self._can_be_afraid and self._morality >= 18 else 0

    @property
    def dexterity(self) -> int:
        return self._personality.dexterity

    def take_damage(self, hp_value: int) -> None:
        self._personality.take_damage(hp_value)

    def demoralize(self, value: int) -> None:
        if self._can_be_afraid:
            self._morality -= value
            if self._morality <= 3:
                self._is_afraid = True

    def inspire(self, value: int) -> None:
        if self._can_be_afraid:
            self._morality += value

