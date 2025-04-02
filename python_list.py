fruits = ["apple", "banana", "cherry"]
fruits.append("orange")   # Adds 'orange' to the list
print(fruits)             # Output: ['apple', 'banana', 'cherry', 'orange']

fruits.insert(1, "grape") # Inserts 'grape' at index 1
print(fruits)             # Output: ['apple', 'grape', 'banana', 'cherry', 'orange']

fruits.remove("banana")   # Removes 'banana'
print(fruits)             # Output: ['apple', 'grape', 'cherry', 'orange']

print(fruits.pop(2))      # Removes and returns 'cherry'
print(fruits)             # Output: ['apple', 'grape', 'orange']

fruits.sort()             # Sorts the list
print(fruits)             # Output: ['apple', 'grape', 'orange']

fruits.reverse()          # Reverses the list
print(fruits)             # Output: ['orange', 'grape', 'apple']
