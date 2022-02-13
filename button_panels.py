from buttons import ElevatorButton, HallButton


class ButtonPanel:
    """
    A class that represents ButtonPanel objects for button panels in elevators and hall.

    parameters:
    panel_id [int]: panel id
    """

    def __init__(self, panel_id: int):
        self._panel_id = panel_id


class ElevatorButtonPanel(ButtonPanel):
    """
    A class that represents ElevatorButtonPanel objects for button panels in elevators.
    This class is inherited from the ButtonPanel class.

    parameters:
    panel_id [int]: a panel id
    available_floor_numbers [dict]: a dictionary that contains the boundaries of the
                                    available floors for the elevator
    buttons [list]: list of objects of class ElevatorButton
    """

    def __init__(self, panel_id, available_floor_numbers: dict):
        super(ElevatorButtonPanel, self).__init__(panel_id)
        self._available_floor_numbers = available_floor_numbers
        self._buttons = dict()
        self._set_up_buttons()

    def _set_up_buttons(self):
        self._buttons = {
            f"{floor_number}": ElevatorButton(
                button_name=str(floor_number), floor_number=floor_number
            )
            for floor_number in range(
                self._available_floor_numbers.get("from_floor"),
                self._available_floor_numbers.get("to_floor") + 1,
            )
        }


class HallButtonPanel(ButtonPanel):
    """
    A class that represents HallButtonPanel objects for button panels in hall.
    This class is inherited from the ButtonPanel class.

    parameters:
    panel_id [int]: a panel id
    is_need_up_button [bool]: up button for the top floor is not created
    is_need_down_button [bool]: down button for the lowest floor is not created
    buttons [list]: list of objects of class ElevatorButton
    """

    def __init__(self, panel_id, is_need_up_button=True, is_need_down_button=True):
        super(HallButtonPanel, self).__init__(panel_id)
        self._is_need_up_button = is_need_up_button
        self._is_need_down_button = is_need_down_button
        self._buttons = dict()
        self._set_up_buttons()

    def _set_up_buttons(self):
        if self._is_need_up_button:
            self._buttons["up"] = HallButton(button_name="Up", direction="up")
        if self._is_need_down_button:
            self._buttons["down"] = HallButton(button_name="Down", direction="down")
