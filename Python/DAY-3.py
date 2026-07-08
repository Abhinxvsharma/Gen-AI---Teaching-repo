# ==========================================
# Python Operators Complete Program
# ==========================================

# ------------------------------------------
# 1. Arithmetic Operators
# ------------------------------------------

# Definition:
# Arithmetic Operators mathematical calculations
# karne ke liye use hote hain.

print("========== Arithmetic Operators ==========")

a = 10
b = 3

print("Addition :", a + b)
print("Subtraction :", a - b)
print("Multiplication :", a * b)
print("Division :", a / b)
print("Floor Division :", a // b)
print("Modulus :", a % b)
print("Exponent :", a ** b)

print()


# ------------------------------------------
# 2. Comparison Operators
# ------------------------------------------

# Definition:
# Comparison Operators do values ko compare karte hain.
# Result hamesha True ya False hota hai.

print("========== Comparison Operators ==========")

x = 10
y = 20

print("x == y :", x == y)
print("x != y :", x != y)
print("x > y :", x > y)
print("x < y :", x < y)
print("x >= y :", x >= y)
print("x <= y :", x <= y)

print()


# ------------------------------------------
# 3. Logical Operators
# ------------------------------------------

# Definition:
# Logical Operators multiple conditions ko combine karte hain.

print("========== Logical Operators ==========")

age = 20
has_id = True

print(age >= 18 and has_id)
print(age >= 18 or has_id)
print(not has_id)

print()


# ------------------------------------------
# 4. Assignment Operators
# ------------------------------------------

# Definition:
# Assignment Operators variable me value assign
# ya update karne ke liye use hote hain.

print("========== Assignment Operators ==========")

score = 10

score += 5
print("After += :", score)

score -= 2
print("After -= :", score)

score *= 2
print("After *= :", score)

score /= 2
print("After /= :", score)

print()


# ------------------------------------------
# 5. Membership Operators
# ------------------------------------------

# Definition:
# Membership Operators check karte hain ki
# koi value sequence ke andar present hai ya nahi.

print("========== Membership Operators ==========")

name = "Rahul"

print("R" in name)
print("z" in name)
print("z" not in name)

print()