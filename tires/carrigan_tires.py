from tires.tires import Tires


class CarriganTires(Tires):
    def __init__(self, tires_status):
        self.tires_status = tires_status

    def needs_service(self):
        for wear_num in self.tires_status:
            if wear_num >= 0.9:
                return True
        return False
