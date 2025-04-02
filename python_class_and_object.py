class Car:  # Class
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")

my_car = Car("Toyota", "Camry")  # Object
my_car.display_info()  # Output: Car Brand: Toyota, Model: Camry
