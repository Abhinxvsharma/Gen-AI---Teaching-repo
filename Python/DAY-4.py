# ==========================================================
#           PYTHON STRINGS - COMPLETE PROGRAM
# ==========================================================

# ----------------------------------------------------------
# 1. STRING
# ----------------------------------------------------------

# Definition:
# String characters (letters, numbers, symbols) ka collection hoti hai.
# String ko Single Quotes (' '), Double Quotes (" ")
# ya Triple Quotes (""" """) ke andar likhte hain.

print("========== STRING ==========")

name = "Python Programming"

print(name)
print(type(name))

print()


# ----------------------------------------------------------
# 2. STRING INDEXING
# ----------------------------------------------------------

# Definition:
# String ka har character ek position (Index) par hota hai.
# Indexing 0 se start hoti hai.

print("========== STRING INDEXING ==========")

print("First Character :", name[0])

print("Second Character :", name[1])

print("Last Character :", name[-1])

print()


# ----------------------------------------------------------
# 3. STRING SLICING
# ----------------------------------------------------------

# Definition:
# String ka chhota part nikalna String Slicing kehlata hai.
#
# Syntax:
# string[start:end]

print("========== STRING SLICING ==========")

print(name[0:6])

print(name[7:18])

print(name[:6])

print(name[7:])

print()


# ----------------------------------------------------------
# 4. SLICING WITH SKIP VALUE
# ----------------------------------------------------------

# Definition:
# Skip Value batati hai kitne characters
# skip karke next character lena hai.
#
# Syntax:
# string[start:end:step]

print("========== SLICING WITH SKIP VALUE ==========")

print(name[0:18:2])

print(name[0:18:3])

print(name[::-1])

print()


# ----------------------------------------------------------
# 5. STRING FUNCTIONS
# ----------------------------------------------------------

# Definition:
# String Functions pre-defined methods hoti hain
# jo string par alag-alag operations karti hain.

print("========== STRING FUNCTIONS ==========")

text = "python programming"

print("Original :", text)

print("Upper :", text.upper())

print("Lower :", text.lower())

print("Title :", text.title())

print("Capitalize :", text.capitalize())

print("Replace :", text.replace("python", "Java"))

print("Find :", text.find("programming"))

print("Count :", text.count("m"))

print("Length :", len(text))

print("Strip :", "   Python   ".strip())

print()


# ----------------------------------------------------------
# 6. ESCAPE SEQUENCE CHARACTERS
# ----------------------------------------------------------

# Definition:
# Escape Sequence Characters special characters hote hain
# jo Backslash (\) se start hote hain.

print("========== ESCAPE SEQUENCE ==========")

print("Hello\nWorld")

print("Python\tProgramming")

print("My name is \"Rahul\"")


print()


# ----------------------------------------------------------
# 7. USER INPUT EXAMPLE
# ----------------------------------------------------------

print("========== USER INPUT ==========")

user = input("Enter Your Name : ")

print("Hello", user)

print("Upper :", user.upper())

print("Lower :", user.lower())

print("Length :", len(user))

print()


