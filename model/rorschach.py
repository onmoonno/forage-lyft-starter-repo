from car import Car
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from tire.carrigan_tire import CarriganTire


class Rorschach(Car):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_worn):
        self.engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.battery = NubbinBattery(last_service_date,current_date)
        self.tire = CarriganTire(tire_worn)
        super().__init__(self.engine, self.battery, self.tire)
