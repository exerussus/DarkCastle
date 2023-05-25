from source.item import Item


class Inventory:

    def __init__(self):
        self._bag_dict = {}
        for i in range(7):
            i += 1
            self._bag_dict[i] = None

    @property
    def bag(self):
        return self._bag_dict

    def _is_correct_index_slot(self, slot_index) -> bool:
        max_slots = len(self._bag_dict)
        return 1 <= slot_index <= max_slots

    def upgrade(self) -> None:
        self._bag_dict[8] = self._bag_dict[9] = None

    def _find_empty_slot(self) -> int:
        for key, value in self._bag_dict.items():
            if value is None:
                return key

    def set_item(self, item: Item) -> None:
        slot_index = self._find_empty_slot()
        self._bag_dict[slot_index] = item

    def delete_item(self, slot_index: int) -> None:
        self._bag_dict[slot_index] = None

    def get_item(self, slot_index: int):
        if self._bag_dict[slot_index] is not None and self._is_correct_index_slot:
            return self._bag_dict[slot_index]
