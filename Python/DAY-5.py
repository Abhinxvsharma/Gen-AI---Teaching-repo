# ===================================================
# LISTS & TUPLES IN PYTHON
# ===================================================

# ---------------------------------------------------
# 1. LIST
# ---------------------------------------------------

# Definition:
# List ek collection hai jo multiple values
# ko ek variable me store karti hai.
# List Mutable hoti hai.

print("========== LIST ==========")

fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits)

print(type(fruits))

print()


# ---------------------------------------------------
# 2. LIST INDEXING
# ---------------------------------------------------

# Definition:
# List ke har element ka ek Index hota hai.

print("========== LIST INDEXING ==========")

print("First Fruit :", fruits[0])

print("Second Fruit :", fruits[1])

print("Last Fruit :", fruits[-1])

print()


# ---------------------------------------------------
# 3. LIST SLICING
# ---------------------------------------------------

# Definition:
# List ka chhota part nikalna List Slicing kehlata hai.

print("========== LIST SLICING ==========")

print(fruits[0:2])

print(fruits[1:4])

print(fruits[:3])

print(fruits[2:])

print()


# ---------------------------------------------------
# 4. LIST METHODS
# ---------------------------------------------------

# Definition:
# List Methods list par operations karne ke liye
# use hote hain.

print("========== LIST METHODS ==========")

numbers = [10, 40, 20, 30]

print("Original :", numbers)

numbers.append(50)
print("Append :", numbers)

numbers.insert(1, 15)
print("Insert :", numbers)

numbers.remove(20)
print("Remove :", numbers)

numbers.pop()
print("Pop :", numbers)

numbers.sort()
print("Sort :", numbers)

numbers.reverse()
print("Reverse :", numbers)

print("Count :", numbers.count(40))

print("Index :", numbers.index(30))

numbers.clear()
print("Clear :", numbers)

print()


# ---------------------------------------------------
# 5. TUPLE
# ---------------------------------------------------

# Definition:
# Tuple ek collection hai jo multiple values
# store karta hai.
# Tuple Immutable hota hai.

print("========== TUPLE ==========")

colors = ("Red", "Green", "Blue", "Yellow")

print(colors)

print(type(colors))

print()


# ---------------------------------------------------
# 6. TUPLE INDEXING
# ---------------------------------------------------

print("========== TUPLE INDEXING ==========")

print(colors[0])

print(colors[2])

print(colors[-1])

print()


# ---------------------------------------------------
# 7. TUPLE METHODS
# ---------------------------------------------------

# Tuple me sirf 2 methods hote hain.

print("========== TUPLE METHODS ==========")

numbers = (10, 20, 30, 20, 40, 20)

print("Count :", numbers.count(20))

print("Index :", numbers.index(30))

print()


# ---------------------------------------------------
# 8. USER INPUT EXAMPLE
# ---------------------------------------------------

print("========== USER INPUT ==========")

name1 = input("Enter First Friend : ")

name2 = input("Enter Second Friend : ")

friend_list = [name1, name2]

print(friend_list)

print()

print("Program Finished Successfully")