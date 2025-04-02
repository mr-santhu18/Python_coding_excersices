# Polymorphism in Python
'''Polymorphism is a fundamental concept 
in object-oriented programming (OOP) that 
allows objects of different classes to be
treated as objects of a common superclass. 
It enables a single interface to be used for
different types, allowing code reusability
 and flexibility.

In Python, polymorphism is mainly implemented in two ways:

1. Method Overriding (Runtime Polymorphism)
2. Method Overloading (Compile-time Polymorphism) – Python does not support it directly.
3. Operator Overloading '''

# Method Overriding (Runtime Polymorphism)
'''
Method overriding occurs when a subclass provides a specific implementation of a method that is already defined in its superclass. 
The overridden method in the subclass should have the same name and parameters as the method in the parent class.
'''

#example
class Animal:
    def speak(self):
        return "Animal makes a sound"

class Dog(Animal):
    def speak(self):
        return "Dog barks"

class Cat(Animal):
    def speak(self):
        return "Cat meows"

# Using Polymorphism
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.speak())


# Method Overloading in Python
'''
Python does not support method overloading like Java or C++.
However, we can achieve a similar effect using default arguments or *args.
'''

# example 

class MathOperations:
    def add(self, a, b, c=0):  # Default argument for handling different cases
        return a + b + c

# Object instantiation
math_op = MathOperations()
print(math_op.add(5, 10))      # Calls add with two arguments
print(math_op.add(5, 10, 15))  # Calls add with three arguments


# Operator Overloading
'''
Python allows the overloading of operators,
meaning that the same operator can have different meanings depending on the context.
'''
# example: Overloading the + Operator
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # Overloading the '+' operator
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2  # Calls the __add__() method
print(p3)  # Output: (6, 8)
