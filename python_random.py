# import random module 
import random

# choose random integer
num = random.randint(1, 10)
print("Random number between 1 and 10:", num)

# Generates a random floating-point number between 0.0 and 1.0.
num = random.random()
print("Random float between 0 and 1:", num)

# Picks a random element from a list, tuple, or string.
colors = ['Red', 'Blue', 'Green', 'Yellow']
choice = random.choice(colors)
print("Random color:", choice)

# Randomly rearranges the elements in a list.
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled list:", numbers)

# Chooses k random elements from a sequence without replacement.
OTP = random.sample(range(0,9), 4)
print("Random OTP numbers:", OTP)
