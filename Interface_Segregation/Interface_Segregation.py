class ParkingInterface:
    def __init__(self, capacity: int) -> None:
        self._capacity = capacity
        
    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, value):
        self._capacity = value
    
    def park_car(self):
        self.capacity -= 1
    
    def unpark_car(self):
        self.capacity += 1


class FreeParkingLot(ParkingInterface):
    def __init__(self, capacity: int) -> None:
        super().__init__(capacity)
    
    def park_car(self):
        return super().park_car()
    
    def unpark_car(self):
        return super().unpark_car()


class PaidParkingLot(ParkingInterface):
    def __init__(self, capacity: int, fee: float, time_amount: str) -> None:
        self.fee = fee
        self.time_amount = time_amount
        super().__init__(capacity)
    
    def calculate_fee(self):
        return f"{self.fee}$ per {self.time_amount}"


class HourlyPaidLot(PaidParkingLot):
    def __init__(self, capacity: int, fee: float, time_amount: str) -> None:
        super().__init__(capacity, fee, time_amount)


class DailyPaidLot(PaidParkingLot):
    def __init__(self, capacity: int, fee: float, time_amount: str) -> None:
        super().__init__(capacity, fee, time_amount)



print("Free parking")
free_parking = FreeParkingLot(8)
print(free_parking.capacity)
free_parking.park_car()
print(free_parking.capacity)
free_parking.unpark_car()
print(free_parking.capacity)

print("hourly paid")
hourly_parking = HourlyPaidLot(10, 5, "hour")
print(hourly_parking.capacity)
hourly_parking.park_car()
print(hourly_parking.capacity)
hourly_parking.unpark_car()
print(hourly_parking.capacity)
print(hourly_parking.calculate_fee())

print("daily paid")
daily_parking = DailyPaidLot(15, 30, "day")
print(daily_parking.capacity)
daily_parking.park_car()
print(daily_parking.capacity)
daily_parking.unpark_car()
print(daily_parking.capacity)
print(daily_parking.calculate_fee())
