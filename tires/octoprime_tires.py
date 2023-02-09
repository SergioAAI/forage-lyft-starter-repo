from tires.tires import Tires


class OctoprimeTires(Tires):
    def __init__(self, tires_status):
        self.tires_status = tires_status

    def needs_service(self):
        total = 0
        for wear_num in self.tires_status:
            total += wear_num
        return total >= 3
