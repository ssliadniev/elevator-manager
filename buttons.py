class Button:
    """
    A class that represents Button objects in a button hall\elevator panels.

    parameters:
    button_name [str]: unique name of button
    """

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
    """
    A class that represents Button objects in a button elevator panels.
    This class is inherited from the Button class.

    parameters:
    button_name [str]: unique name of button
    floor_number [int]: building floor number
    """

    def __init__(self, button_name: str, floor_number: int):
        super(ElevatorButton, self).__init__(button_name)
        self._floor_number = floor_number


class HallButton(Button):
    """
    A class that represents Button objects in a button hall panels.
    This class is inherited from the Button class.

    parameters:
    button_name [str]: unique name of button
    floor [int]: building floor number
    """

    def __init__(self, button_name: str, direction: str):
        super(HallButton, self).__init__(button_name)
        self._direction = direction

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, direction):
        available_directions = ("up", "down")
        if direction.upper() not in available_directions:
            raise ValueError(
                f"Error. Set wrong direction: '{direction}'.\nAvailable directions: up, down."
            )
        self._direction = direction
