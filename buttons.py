class Button:
    def __init__(self):
        self.__on = False

    def change_state(self, new_state: bool):
        if isinstance(new_state, bool):
            self.__on = new_state

    def get_state(self):
        return self.__on

    def __str__(self):
        return f"{self.__on}"


class ElevatorButton(Button):
    def __init__(self, floor: int):
        super(ElevatorButton, self).__init__()
        self.floor = floor


class HallButton(Button):
    def __init__(self, direction: str):
        super(HallButton, self).__init__()
        self.direction = direction
