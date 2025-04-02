# series 
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)

# print var in my series

print(myvar[0])

# create lables
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)

# accessing with the help of index value
print(myvar["y"])

# Key value pairs with the help of pandas
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)





