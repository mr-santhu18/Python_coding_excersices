# install numpy

'''pip install numpy'''

# check the numpy version
"""
import numpy as np

print(np.__version__) """

# imprt numpy lib and creating one dimentional array
'''import numpy

 arr = numpy.array([1, 2, 3, 4, 5])

print(arr)

'''

# 2D array
'''import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print(arr1 + arr2)'''

# creating a one dimentional array using numpy and 
"""
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))
"""

# Use a tuple to create a NumPy array:

'''import numpy as np

arr = np.array((1, 2, 3, 4, 5))

print(arr)'''

# ARRAY INDEXING

# Get the first element from the following array:

''' import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0]) '''

# Get third and fourth elements from the following array and add them.

''' import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[2] + arr[3]) '''

 # Access the element on the first row, second column:

'''import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print(arr)
print('2nd element on 1st row: ', arr[1, 1]) '''

# Access the third element of the second array of the first array:

'''import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr)
print(arr[0, 1, 2])'''

# ARRAY SLICING

# Slice elements from index 1 to index 5 from the following array:

'''import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])'''

# Slice from the index 3 from the end to index 1 from the end:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-1])



