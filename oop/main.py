class Car:
    # class attribute
    total_cars = 0

    # constructor function
    def __init__(self, brand, model):
        self.brand = brand  # attribute
        self.model = model  # attribute
        Car.total_cars += 1

    def get_car_details(self):
        print(f"Brand {self.brand} Model {self.model}")

    # static method -> methods that belongs to class rather than object
    # Static methods can't access or modify class or instance variables directly

    @staticmethod
    # we cant provide self as argument in static methods
    def get_general_description():
        print("This will print the general description of the car.")


# creating object

car = Car("Tata", "Nexon")

print(car.brand)
print(car.model)
car.get_car_details()


Car.total_cars

Car.get_general_description()
