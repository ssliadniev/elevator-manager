import floors
import elevators


class Build:
    def __init__(self, min_floor, max_floor, elevator_number):
        self._min_floor = min_floor
        self._max_floor = max_floor
        self._elevator_number = elevator_number
        self._floors: list = []
        self._elevators: list = []
        self.create_floor_objects()
        self.create_elevators_objects()

    def create_floor_objects(self):
        for floor_number in range(self._min_floor, self._max_floor + 1):
            if floor_number == self._min_floor:
                self._floors.append(floors.Floor(floor_number=floor_number, down_flag=False))
            elif floor_number == self._max_floor:
                self._floors.append(floors.Floor(floor_number=floor_number, up_flag=False))
            else:
                self._floors.append(floors.Floor(floor_number=floor_number))

    def create_elevators_objects(self):
        self._elevators = [
            elevators.Elevator(elevator_id)
            for elevator_id in range(self._elevator_number)
        ]

    def get_floor_count(self):
        return self._max_floor + abs(self._min_floor)

    def get_min_max_floor(self):
        return {"min": self._min_floor, "max": self._max_floor}
