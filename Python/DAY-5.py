# ==========================================
# WHILE LOOP - COMPLETE PROGRAM
# ==========================================

# ------------------------------------------
# 1. Basic While Loop
# ------------------------------------------

# Definition:
# while loop tab tak chalta hai
# jab tak condition True hoti hai.

# Count = Counter Variable ek variable hota hai jo loop kitni baar chala hai uska count rakhta hai.

print("========== Basic While Loop ==========")

count = 1

while count <= 5:
    print(count)
    count += 1

print()


# ------------------------------------------
# 2. Infinite Loop Example
# ------------------------------------------

# Definition:
# Agar counter update nahi hota
# to loop kabhi khatam nahi hota.
# Isse Infinite Loop kehte hain.

print("========== Infinite Loop Example ==========")

print("Example Only (Don't Run)")

# count = 1

# while count <= 5:
#     print(count)

# count += 1 missing hai


print()


# ------------------------------------------
# 3. User Password Example
# ------------------------------------------

print("========== Password Example ==========")

password = ""

while password != "1234":

    password = input("Enter Password : ")

print("Access Granted")

print()


# ------------------------------------------
# 4. Sum of Numbers
# ------------------------------------------

# Definition:
# total = Accumulator Variable total ko use karke
# values ko add karte hain.

print("========== Sum Example ==========")

total = 0

count = 1

while count <= 5:

    total = total + count

    count += 1

print("Sum =", total)

print()


# ------------------------------------------
# 5. while True + break
# ------------------------------------------

# break = loop ko turant stop kar deta hai

print("========== while True Example ==========")

while True:

    value = input("Enter Anything (type stop to exit): ")

    if value == "stop":
        break

    print("You Entered :", value)

print("Loop Ended")

print()


# ------------------------------------------
# 6. Number Guessing Game
# ------------------------------------------

print("========== Guessing Game ==========")

secret_number = 7

guess = int(input("Guess Number (1-10): "))

attempt = 1

while guess != secret_number:

    print("Wrong Guess")

    guess = int(input("Try Again : "))

    attempt += 1

print("Correct!")

print("Attempts :", attempt)

print()


# ------------------------------------------
# 7. Table Program
# ------------------------------------------

print("========== Table Program ==========")

num = int(input("Enter Number : "))

i = 1

while i <= 10:

    print(num, "x", i, "=", num * i)

    i += 1

print()

print("Program Finished Successfully.")