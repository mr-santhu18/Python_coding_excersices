# Data Abstraction in Python

'''
What is Data Abstraction?
Data abstraction is an object-oriented programming (OOP) concept that hides the implementation details from the user and only exposes the necessary functionalities. This helps in reducing complexity and increases code reusability.

In Python, abstraction can be achieved using abstract classes and abstract methods provided by the abc (Abstract Base Class) module.
'''
'''
How to Implement Abstraction in Python?
Use the ABC class from the abc module.
Define an abstract method using the @abstractmethod decorator.
Create a subclass that provides implementations for all abstract methods.
'''
# example
from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    
    @abstractmethod
    def start(self):
        """Abstract method (must be implemented in subclasses)"""
        pass
    
    @abstractmethod
    def stop(self):
        """Abstract method (must be implemented in subclasses)"""
        pass

# Concrete class implementing the abstract methods
class Car(Vehicle):
    
    def start(self):
        print("Car engine started.")
    
    def stop(self):
        print("Car engine stopped.")

# Concrete class implementing the abstract methods
class Bike(Vehicle):
    
    def start(self):
        print("Bike engine started.")
    
    def stop(self):
        print("Bike engine stopped.")

# Creating objects
my_car = Car()
my_car.start()  # Output: Car engine started.
my_car.stop()   # Output: Car engine stopped.

my_bike = Bike()
my_bike.start()  # Output: Bike engine started.
my_bike.stop()   # Output: Bike engine stopped.


# benefits of data abstraction
'''
1. Encapsulation of Implementation Details: Hides the implementation and only exposes necessary details.
2. Flexibility and Scalability: New subclasses can be added without modifying the abstract class.
3. Code Reusability: Common behaviors are defined in the abstract class, reducing redundancy.
'''