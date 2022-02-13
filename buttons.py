class Button:
    def __init__(self, button_name: str):
        self._button_name = button_name
        self.__on = False

    def press_down(self, new_state: bool = True):
        if isinstance(new_state, bool):
            self.__on = new_state

    def is_pressed(self):
        return self.__on

    def get_state(self):
        return self.__on

    def __str__(self):
        return f"{self._button_name}"


class ElevatorButton(Button):
    def __init__(self, button_name: str, floor: int):
        super(ElevatorButton, self).__init__(button_name)
        self._floor = floor


class HallButton(Button):
    def __init__(self, button_name: str, direction: str):
        super(HallButton, self).__init__(button_name)
        self._direction = direction
