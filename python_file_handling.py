# syntax

# file = open("filename","mode")

'''
r- read mode 
w- write mode
a- append mode 
x- exclusive creation mode
r+  read + write
w+ write + read
a+ append + read  
'''
 # exaple for w mode 
# file = open("sample.txt","w")

# file.write("this is a new file.\n")
# file.write("python is programming lang")
# file.close()

# read mode

# file = open("sample.txt","r")

# content = file.read()

# print(content)
# file.close()


# methods in read mode
'''
file.read(size)
file.readline()
file.readlines()
'''

# append mode

''' file = open("sample.txt","a")
file.write("/n appending line....!")
file.close() '''

# using with statement 

''' with open("sample.txt","r") as file:
    content = file.read()
    print(content)'''

# binary files
# rb- read binary
# wb- write binary

# with open ("image.jpg","rb") as file:
#     binary_data = file.read()
#     print(binary_data[:20])


# import os
# if os.path.exists("sample.txt"):
#     print("file is exist")
# else :
#     print("file is not found")

# import os
# if os.path.exists("sample.txt"):
#     os.remove("sample.txt")
#     print("file deleted..!")
# else:
#     print("file not found..!")
