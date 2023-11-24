from car import Car
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery
from tire.octoprime_tire import OctoprimeTire


class Glissade(Car):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_worn):
        self.engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.battery = SpindlerBattery(last_service_date, current_date)
        self.tire = OctoprimeTire(tire_worn)
        super().__init__(self.engine, self.battery, self.tire)

