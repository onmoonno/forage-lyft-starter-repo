from car import Car
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from tire.carrigan_tire import CarriganTire



class Palindrome(Car):
    def __init__(self, current_date, last_service_date, warning_light_on, tire_worn):
        self.engine = SternmanEngine(warning_light_on)
        self.battery = SpindlerBattery(last_service_date, current_date)
        self.tire = CarriganTire(tire_worn)
        super().__init__(self.engine, self.battery, self.tire)

