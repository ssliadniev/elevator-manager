class Request:
    def __init__(self, pushed_hall_button, pushed_elevator_button):
        self._pushed_hall_button = pushed_hall_button
        self._target_floor = pushed_elevator_button
