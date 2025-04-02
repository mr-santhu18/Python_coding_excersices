text = " Hello, Python! "
print(len(text))         # Output: 15
print(text.upper())      # Output: " HELLO, PYTHON! "
print(text.lower())      # Output : "hello, world!"
print(text.strip())      # Output: "Hello, Python!"
print(text.replace("Python", "World"))  # Output: " Hello, World! "
print(text.split(","))   # Output: [' Hello', ' Python! ']
print(text[0:5])  #string slicing [ Hell]
result = text[::-1] # reverse string
print(result)