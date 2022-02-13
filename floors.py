from button_panels import HallButtonPanel


class Floor:
    """
    A class that represents Floor objects in a building.

    parameters:
    floor_number [int]: current floor number
    lowest_floor [int]: lowest floor of building
    highest_floor [int]: highest floor of building
    button_panel [HallButtonPanel object]: an object that represents the hall button panel
    """

    def __init__(self, floor_number: int, lowest_floor: int, highest_floor: int):
        self._floor_number = floor_number
        self._lowest_floor = lowest_floor
        self._highest_floor = highest_floor
        self._button_panel = HallButtonPanel(
            panel_id=floor_number,
            is_need_up_button=self.is_need_up_button(),
            is_need_down_button=self.is_need_down_button(),
        )

    def is_need_up_button(self):
        return self._floor_number != self._highest_floor

    def is_need_down_button(self):
        return self._floor_number != self._lowest_floor

    def get_floor_number(self):
        return self._floor_number
