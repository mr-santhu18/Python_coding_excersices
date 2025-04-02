my_set = {1, 2, 3, 4}
print(my_set)   # Output: {1, 2, 3, 4}

empty_set = set()  # Creates an empty set (not {})
print(empty_set)   # Output: set()

numbers = {1, 2, 3}
numbers.add(4)
print(numbers)  # Output: {1, 2, 3, 4}

numbers.update([5, 6, 7])
print(numbers)  # Output: {1, 2, 3, 4, 5, 6, 7}

numbers = {1, 2, 3, 4, 5}
numbers.remove(3)
print(numbers)  # Output: {1, 2, 4, 5}

numbers.discard(10)  # No error, even though 10 is not in the set

numbers.pop()   # Removes a random element
print(numbers)  

numbers.clear() # Removes all elements
print(numbers)  # Output: set()

A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)          # Output: {1, 2, 3, 4, 5}
print(A.union(B))     # Output: {1, 2, 3, 4, 5}

print(A & B)          # Output: {3}
print(A.intersection(B))  # Output: {3}

print(A - B)          # Output: {1, 2}
print(A.difference(B))  # Output: {1, 2}

print(A ^ B)          # Output: {1, 2, 4, 5}
print(A.symmetric_difference(B))  # Output: {1, 2, 4, 5}

A = {1, 2}
B = {1, 2, 3, 4}

print(A.issubset(B))  # Output: True
print(B.issuperset(A)) # Output: True
print(A.isdisjoint({5, 6})) # Output: True (No common elements)
