student = {
    "name": "santhu",
    "age": 26,
    "course": "Python"
}

print(student.keys())     # Output: dict_keys(['name', 'age', 'course'])
print(student.values())   # Output: dict_values(['santhu', 21, 'Python'])
print(student.items())    # Output: dict_items([('name', 'santhu'), ('age', 26), ('course', 'Python')])
print(student.get("age")) # Output: 26
student.update({"city": "Bangalore"})
print(student)            # Output: {'name': 'santhu', 'age': 26, 'course': 'Python', 'city': 'Bangalore'}
