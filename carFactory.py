from datetime import date
from model.calliope import Calliope
from model.glissade import Glissade
from model.palindrome import Palindrome
from model.rorschach import Rorschach
from model.thovex import Thovex


class CarFactory:
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Calliope:
        car = Calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        return car

    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Glissade:
        car = Glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        return car

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_is_on: bool) -> Palindrome:
        car = Palindrome(current_date, last_service_date, warning_light_is_on)
        return car

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Rorschach:
        car = Rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
        return car

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Thovex:
        car = Thovex(current_date, last_service_date, current_mileage, last_service_mileage)
        return car
