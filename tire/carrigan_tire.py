from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, tire_worn):
        super().__init__(tire_worn)

    def needs_service(self):
        for worn in self.tire_worn:
            if worn >= 0.9:
                return True

        return False
