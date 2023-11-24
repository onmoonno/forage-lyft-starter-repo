from datetime import date
from model.calliope import Calliope
from model.glissade import Glissade
from model.palindrome import Palindrome
from model.rorschach import Rorschach
from model.thovex import Thovex


class CarFactory:
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_worn: [float]) -> Calliope:
        car = Calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_worn)
        return car

    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_worn: [float]) -> Glissade:
        car = Glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_worn)
        return car

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_is_on: bool, tire_worn: [float]) -> Palindrome:
        car = Palindrome(current_date, last_service_date, warning_light_is_on, tire_worn)
        return car

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_worn: [float]) -> Rorschach:
        car = Rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_worn)
        return car

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_worn: [float]) -> Thovex:
        car = Thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_worn)
        return car
