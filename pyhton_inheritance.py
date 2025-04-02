# Inheritance in Python
''' 
Inheritance is one of the fundamental concepts of Object-Oriented Programming (OOP). 
It allows a class (child or derived class) to inherit properties and behaviors (methods) 
from another class (parent or base class). This promotes code reusability, modularity,
 and hierarchical classification.
'''

# types of inheritance in pyhton
# single inheritance 
'''
A child class inherits from a single parent class.
The child class can access methods and attributes of the parent class.
'''
'''
Animal (Parent)
   ↑
   |
Dog (Child)

'''
# example

'''
class Animal:
    def speak(self):
        return "Animal makes a sound"

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        return "Dog barks"

dog = Dog()
print(dog.speak())  # Inherited method
print(dog.bark())   # Dog class method
'''



# multiple inheritance
'''
A child class inherits from multiple parent classes.
'''

'''
Father       Mother
   \         /
    \       /
     \     /
      Child

'''

# example

class Father:
    def skill1(self):
        return "Father: Knows Gardening"

class Mother:
    def skill2(self):
        return "Mother: Knows Cooking"

class Child(Father, Mother):  # Inheriting from both Father and Mother
    def skill3(self):
        return "Child: Knows Painting"

c = Child()
print(c.skill1())  # Inherited from Father
print(c.skill2())  # Inherited from Mother
print(c.skill3())  # Own method



# Multilevel Inheritance
'''
A child class inherits from another child class, creating a chain.
'''

'''
Grandparent
     ↓
   Parent
     ↓
   Child

'''
# exaple 

class Grandparent:
    def family_history(self):
        return "Grandparent: Strong Family Lineage"

class Parent(Grandparent):  # Inherits from Grandparent
    def advice(self):
        return "Parent: Study Well"

class Child(Parent):  # Inherits from Parent
    def play(self):
        return "Child: Loves Playing"

c = Child()
print(c.family_history())  # Inherited from Grandparent
print(c.advice())          # Inherited from Parent
print(c.play())            # Own method



#  Hierarchical Inheritance
'''
Multiple child classes inherit from a single parent class.
''' 

'''
      Vehicle
      /     \
    Car     Bike

'''

# example

class Vehicle:
    def engine(self):
        return "Vehicle has an engine"

class Car(Vehicle):  # Inherits from Vehicle
    def wheels(self):
        return "Car has 4 wheels"

class Bike(Vehicle):  # Inherits from Vehicle
    def wheels(self):
        return "Bike has 2 wheels"

c = Car()
b = Bike()
print(c.engine(), "-", c.wheels())  # Inherited and own method
print(b.engine(), "-", b.wheels())  # Inherited and own method



# Hybrid Inheritance
'''
A mix of two or more types of inheritance.
'''

'''
       A
      / \
     B   C
      \ /
       D

'''

# Example

class A:
    def methodA(self):
        return "Class A method"

class B(A):  # Single Inheritance
    def methodB(self):
        return "Class B method"

class C(A):  # Single Inheritance
    def methodC(self):
        return "Class C method"

class D(B, C):  # Multiple Inheritance
    def methodD(self):
        return "Class D method"

d = D()
print(d.methodA())  # Inherited from A
print(d.methodB())  # Inherited from B
print(d.methodC())  # Inherited from C
print(d.methodD())  # Own method

