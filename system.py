from building import Build
from elevators import Elevator


class ElevatorSystem:
    def __init__(self, lowest_floor, highest_floor, elevator_count):
        self._min_floor = lowest_floor
        self._max_floor = highest_floor
        self._elevator_number = elevator_count
        self._elevators = list()
        self._requests = list()
        self._build = Build(
            lowest_floor=lowest_floor,
            highest_floor=highest_floor,
            elevator_count=elevator_count,
        )
        self.__create_elevators_objects()

    def __create_elevators_objects(self):
        self._elevators = [
            Elevator(elevator_id) for elevator_id in range(self._elevator_number)
        ]
