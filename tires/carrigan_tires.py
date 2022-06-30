from tires.tires import Tires


class CarriganTires(Tires):
    def __init__(self, wear_array):
        self.wear_array = wear_array

    def needs_service(self):
        for wear in self.wear_array:
            if wear >= 0.9:
                return True
        return False