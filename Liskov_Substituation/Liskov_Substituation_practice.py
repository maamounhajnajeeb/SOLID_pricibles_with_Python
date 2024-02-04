class MotoCycle:
    def __init__(self, wheels: int, type_of_fuel: str) -> None:
        self.type_of_fuel = type_of_fuel
        self.wheels = wheels
    
    def get_all_details(self):
        return f"number of wheels: {self.wheels}, type of fuel: {self.type_of_fuel}"


class Bycycle:
    def __init__(self, wheels: int, ) -> None:
        self.wheels = wheels
    
    def get_all_details(self):
        return f"number of wheels: {self.wheels}, type of fuel: {self.type_of_fuel}"
