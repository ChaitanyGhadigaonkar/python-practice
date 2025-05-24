from main import Car


class EngineCar(Car):  # Extending the car class

    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize


class DieselCar(Car):  # Extending the car class

    def __init__(self, brand, model, tankCapacity):
        super().__init__(brand, model)
        tankCapacity.batterySize = tankCapacity


engineCar = EngineCar("Tata", "Nexon", "30kwh")

engineCar.get_car_details()
print(engineCar.brand)
print(engineCar.model)
print(engineCar.batterySize)
