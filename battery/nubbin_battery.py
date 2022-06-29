from abc import ABC

from car import Car

from datetime import datetime


class NubbinBattery(Car, ABC):
    def __init__(self, last_service_date):
        super().__init__(last_service_date)

    def needs_serviced(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.needs_serviced():
            return True
        else:
            return False