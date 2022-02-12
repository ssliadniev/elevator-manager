from buttons import HallButton


class Floor:
    def __init__(self, floor_number: int, up_flag: bool = True, down_flag: bool = True):
        self.floor_number = floor_number
        self.up_flag = up_flag
        self.down_flag = down_flag
        self._set_up_buttons()

    def _set_up_buttons(self):
        if self.up_flag:
            self.up_button = HallButton("UP")
        if self.down_flag:
            self.down_button = HallButton("DOWN")
