class Door:
    def __init__(self, id_door, is_open=False):
        self._id_door = id_door
        self._is_open = is_open

    def open(self):
        self._is_open = True

    def close(self):
        self._is_open = False

    def is_open(self):
        return self._is_open
