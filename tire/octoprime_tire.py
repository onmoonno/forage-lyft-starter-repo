from tire.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, tire_worn):
        super().__init__(tire_worn)

    def needs_service(self):
        return sum(self.tire_worn) >= 3