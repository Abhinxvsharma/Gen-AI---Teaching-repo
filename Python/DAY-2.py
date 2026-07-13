# # -------------------------------------------------
# # 1. MODULES
# # -------------------------------------------------

# # Definition:
# # A Module is a file that contains pre-written Python code.
# # We import modules when we want to use their functions.

import math
import keyword

print("========== MODULE EXAMPLE ==========")

print("Square Root of 64 =", math.sqrt(64))
print("Value of PI =", math.pi)

print()
# # 

# # -------------------------------------------------
# # 2. PIP
# # -------------------------------------------------

# # Definition:
# # pip stands for "Pip Installs Packages".
# # It is Python's package manager.
# # It is used to install external libraries.

# # Examples (Run these commands in Terminal, NOT in Python)

# # pip install numpy
# # pip install pandas
# # pip uninstall numpy
# # pip list

print("========== PIP ==========")
print("PIP commands are executed in Terminal.")
print()


# # -------------------------------------------------
# # 3. INPUT()
# # -------------------------------------------------

# # Definition:
# # input() is used to take input from the user.
# # By default, input() always returns data as a STRING.

print("========== INPUT FUNCTION ==========")

name = input("Enter Your Name : ")
age = input("Enter Your Age : ")

print()


# # -------------------------------------------------
# # 4. TYPE()
# # -------------------------------------------------

# # Definition:
# # type() tells us the data type of a variable.

print("========== TYPE FUNCTION ==========")

print(type(name))
print(type(age))

print()


# # -------------------------------------------------
# # 5. TYPE CASTING
# # -------------------------------------------------

# # Definition:
# # Type Casting means converting one data type into another.

age = int(age)

print("========== TYPE CASTING ==========")

print(type(age))

height = float(input("Enter Your Height : "))

print(type(height))

number = str(100)

print(number)
print(type(number))

print()


# # -------------------------------------------------
# # 6. INDENTATION
# # -------------------------------------------------

# # Definition:
# # Indentation means giving spaces before a line of code.
# # Python uses indentation to identify blocks of code.

# print("========== INDENTATION ==========")

if age >= 18:
    print(name, "is Eligible to Vote")
else:
    print(name, "is Not Eligible to Vote")

print()


# -------------------------------------------------
# 7. KEYWORDS
# -------------------------------------------------

# Definition:
# Keywords are reserved words in Python.
# They already have special meanings.
# We cannot use them as variable names.

print("========== PYTHON KEYWORDS ==========")

print(keyword.kwlist)

print()


# -------------------------------------------------
# FINAL OUTPUT
# -------------------------------------------------

# print("========== STUDENT DETAILS ==========")

print("Name :", name)
print("Age :", age)
print("Height :", height)

print()

print("Program Finished Successfully.")



# ==================================
# Arithmetic Operators in Python
# ==================================

num1 = 20
num2 = 6

print("First Number :", num1)
print("Second Number :", num2)

print()

# Addition
print("Addition :", num1 + num2)

# Subtraction
print("Subtraction :", num1 - num2)

# Multiplication
print("Multiplication :", num1 * num2)

# Division
print("Division :", num1 / num2)

# Floor Division
print("Floor Division :", num1 // num2)

# Modulus  (Remainder)
print("Remainder :", num1 % num2)




# NOTES :


# Module  -	Module ek Python file hoti hai jisme pehle se likha hua code hota hai jise hum import karke use karte hain.

# pip	  -  pip Python ka Package Manager hai jisse hum naye packages install karte hain.

# input() -	input() user se data lene ke liye use hota hai aur hamesha String return karta hai.

# type()  - type() batata hai variable ka data type kya hai.

# Type Casting	- Ek data type ko dusre data type mein convert karna Type Casting kehlata hai.

# Indentation  - Code ke shuru mein spaces dena Indentation kehlata hai, jo Python mein code blocks define karta hai.

# Keywords - Keywords Python ke Reserved Words hote hain jinhe variable naam ke roop mein use nahi kar sakte.