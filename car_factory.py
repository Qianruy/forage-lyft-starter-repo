from car import Car
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, wear_array):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTires(wear_array)
        return Car(engine, battery, tires)

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, wear_array):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTires(wear_array)
        return Car(engine, battery, tires)

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on, wear_array):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTires(wear_array)
        return Car(engine, battery, tires)

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, wear_array):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = OctoprimeTires(wear_array)
        return Car(engine, battery, tires)

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, wear_array):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = OctoprimeTires(wear_array)
        return Car(engine, battery, tires)
