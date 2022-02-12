from building import Build


class ElevatorSystem:

    def __init__(self, min_floor, max_floor, elevator_number):
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.build = Build(min_floor=min_floor, max_floor=max_floor, elevator_number=elevator_number)


if __name__ == "__main__":
    launch_system = ElevatorSystem(min_floor=-2, max_floor=40, elevator_number=2)
    print(launch_system)