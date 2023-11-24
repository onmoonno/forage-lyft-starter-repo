from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from car import Car


class Palindrome(Car):
    def __init__(self, current_date, last_service_date, warning_light_on):
        self.engine = SternmanEngine(warning_light_on)
        self.battery = SpindlerBattery(last_service_date, current_date)
        super().__init__(self.engine, self.battery)

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()