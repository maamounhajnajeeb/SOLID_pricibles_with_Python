class MotoCycle:
    def __init__(self, wheels: int, type_of_fuel: str) -> None:
        self.type_of_fuel = type_of_fuel
        self.wheels = wheels
    
    def get_all_details(self):
        return f"number of wheels: {self.wheels}, type of fuel: {self.type_of_fuel}"


class Bycycle:
    def __init__(self, wheels: int, kind: str) -> None:
        self.wheels = wheels
        self.kind = kind
    
    def get_all_details(self):
        return f"number of wheels: {self.wheels}, type of bicycle: {self.kind}"


class BMXBicycle(Bycycle):
    def __init__(self, wheels: int, kind: str) -> None:
        super().__init__(wheels, kind)


bmx = BMXBicycle(2, "bmx")
print(bmx.get_all_details())

motor_4X4 = MotoCycle(4, "Gazoline")
print(motor_4X4.get_all_details())

harley = MotoCycle(2, "Diesel")
print(harley.get_all_details())
