class Elevator:
    def __init__(
        self,
        elevator_id,
        status="Stop",
        limit_weight=None,
        limit_people=None,
        max_speed=None,
    ):
        self.elevator_id = elevator_id
        self.status = status
        self.limit_weight = limit_weight
        self.limit_people = limit_people
        self.max_speed = max_speed
