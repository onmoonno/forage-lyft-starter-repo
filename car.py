from abc import ABC


class Car(ABC):
    def __init__(self, engine, battery, tire):
        """
        Initialize a Car with specified engine, battery, and tire.
        """
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def needs_service(self):
        """
        Check if the car needs service based on its components.
        """
        return self.engine.needs_service() or self.battery.needs_service() or self.tire.needs_service()

