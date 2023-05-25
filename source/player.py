from source.inventory import Inventory
from source.item import Item
from source.personality import Personality


class Player:

    def __init__(self, personality: Personality, inventory: Inventory):
        self._personality = personality
        self._inventory = inventory

    @property
    def name(self) -> bool:
        return self._personality.name

    @property
    def is_alive(self) -> bool:
        return self._personality.is_alive

    @property
    def attack_damage(self) -> int:
        return self._personality.attack_damage

    @property
    def dexterity(self) -> int:
        return self._personality.dexterity

    def take_damage(self, hp_value: int) -> None:
        self._personality.take_damage(hp_value)

    def take_item(self, item: Item):
        self._inventory.set_item(item)

    def use_item(self, slot_index: int) -> int:
        transition_value = self._inventory.get_item(slot_index)
        self._inventory.delete_item(slot_index)
        return transition_value

