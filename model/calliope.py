from car import Car
from engine.capulet_engine import CapuletEngine
from battery.spindler_battery import SpindlerBattery
from tire.octoprime_tire import OctoprimeTire


class Calliope(Car):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_worn):
        self.engine = CapuletEngine(current_mileage, last_service_mileage)
        self.battery = SpindlerBattery(last_service_date, current_date)
        self.tire = OctoprimeTire(tire_worn)
        super().__init__(self.engine, self.battery, self.tire)
