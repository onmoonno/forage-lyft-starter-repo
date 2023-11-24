from engine.capulet_engine import CapuletEngine
from battery.spindler_battery import SpindlerBattery
from car import Car


class Calliope(Car):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.engine = CapuletEngine(current_mileage, last_service_mileage)
        self.battery = SpindlerBattery(last_service_date, current_date)
        super().__init__(self.engine, self.battery)

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
