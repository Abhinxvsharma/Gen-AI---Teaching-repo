# ======================================================
# DICTIONARY & SETS IN PYTHON
# ======================================================

# ------------------------------------------------------
# 1. Dictionary
# ------------------------------------------------------

# Definition:
# Dictionary data ko Key : Value pair me store karti hai.

print("========== DICTIONARY ==========")

student = {
    "name":"Rahul",
    "age":20,
    "course":"Python",
    "city":"Delhi"
}

print(student)

print(type(student))

print()

# ------------------------------------------------------
# Access Dictionary
# ------------------------------------------------------

print("========== ACCESS DICTIONARY ==========")

print(student["name"])

print(student["age"])

print(student.get("city"))

print()

# ------------------------------------------------------
# Dictionary Methods
# ------------------------------------------------------

print("========== DICTIONARY METHODS ==========")

print(student.keys())

print(student.values())

print(student.items())

student.update({"age":21})

print(student)

student.pop("city")

print(student)

print()

# ------------------------------------------------------
# Set
# ------------------------------------------------------

# Definition:
# Set Unique Values Store karta hai.

print("========== SET ==========")

numbers = {10,20,30,40,20,30}

print(numbers)

print(type(numbers))

print()

# ------------------------------------------------------
# Set Methods
# ------------------------------------------------------

print("========== SET METHODS ==========")

numbers.add(50)

print(numbers)

numbers.remove(20)

print(numbers)

numbers.pop()

print(numbers)

print()

# ------------------------------------------------------
# Set Operations
# ------------------------------------------------------

print("========== SET OPERATIONS ==========")

set1 = {1,2,3,4}

set2 = {3,4,5,6}

print("Union :", set1.union(set2))

print("Intersection :", set1.intersection(set2))

print("Difference :", set1.difference(set2))

print("Symmetric Difference :",
      set1.symmetric_difference(set2))

print()

# ------------------------------------------------------
# User Example
# ------------------------------------------------------

print("========== USER INPUT ==========")

name = input("Enter Name : ")

age = input("Enter Age : ")

student = {
    "Name":name,
    "Age":age
}

print(student)

print()

print("Program Finished Successfully")