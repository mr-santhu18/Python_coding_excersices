# syntax

''' 
def function_name(parameters):
    statements
    return values
    '''

# example

'''def greet():
    print("hello world..!")
greet()'''

'''def greet(name):
    print(f"hello, {name}..!")
greet("MCA")'''

'''def add(a,b):
    return a+b
result = add(5,10)
print("sum :",result)'''

# default parameters
'''def greet(name = "guest"):
    print(f"hello, {name}!")

greet()
greet("Arjun")'''

# function with return values

def square(num):
    return num * num
result = square(4)
print("square is :",result)
