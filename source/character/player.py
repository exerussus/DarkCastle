from source.inventory.inventory import Inventory
from source.inventory.inventory import Item
from source.character.character import Character


class Player:

    def __init__(self, character: Character, inventory: Inventory):
        self._character = character
        self._inventory = inventory

    @property
    def inventory(self) -> Inventory:
        return self._inventory

    @property
    def character(self) -> Character:
        return self._character

    def take_item(self, item: Item):
        self._inventory.set_item(item)

    def use_item(self, slot_index: int) -> int:
        transition_value = self._inventory.get_item(slot_index)
        self._inventory.delete_item(slot_index)
        return transition_value

    def get_spend_gold_if_enough(self, cost_value: int) -> bool:
        if self._inventory.gold.get_is_gold_enough(cost_value):
            self._inventory.gold.spend_gold(cost_value)
            return True
        else:
            return False
