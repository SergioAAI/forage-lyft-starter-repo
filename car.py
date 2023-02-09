from serviceable import Serviceable
from engine import engine
from battery import battery


class Car(Serviceable):
    def __init__(self, engine_given:engine, battery_given:battery):
        self.engine = engine_given
        self.battery = battery_given

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
