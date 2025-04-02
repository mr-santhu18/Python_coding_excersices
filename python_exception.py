'''
2. Exception Handling Keywords in Python
Python provides several keywords to handle exceptions:

Keyword	Description
try	- Code that may raise an exception is placed inside a try block.
except - This block handles the exception if it occurs.
else -	Executes if no exceptions occur in the try block.
finally - This block is executed no matter what (exception occurs or not).

'''

# Basic Example of Exception Handling
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2  # Might cause ZeroDivisionError
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input! Please enter numeric values.")
else:
    print("Division successful.")
finally:
    print("Execution completed.")
 