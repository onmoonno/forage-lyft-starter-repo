from abc import ABC, abstractmethod


class Tire(ABC):
    def __init__(self, tire_worn: [float]):
        self.tire_worn = tire_worn

    @abstractmethod
    def needs_service(self):
        pass
