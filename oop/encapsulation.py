class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model
        # __ to make attribute private now __model is a private variable and only accessible inside the class

    def __get_car_details(self):  # private method
        print(f"Brand {self.brand} Model {self.__model}")

    def get_model(self):  # getter function for the private variable model
        return self.__model

    def set_model(self, new_model):  # setter function to set the value of private variables
        self.__model = new_model


# creating object
car = Car("Tata", "Nexon")

print(car.brand)
# this will throw error AttributeError: 'Car' object has no attribute '__model'
# print(car.__model)
car.__get_car_details()  # This will raise an AttributeError
car._Car__get_car_details()
