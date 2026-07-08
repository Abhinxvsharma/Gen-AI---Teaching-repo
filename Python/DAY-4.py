# ============================================
# Conditional Statements in Python
# ============================================

# --------------------------------------------
# 1. IF Statement
# --------------------------------------------

# Definition:
# if statement condition ko check karta hai.
# Agar condition True ho to if block execute hota hai.

print("========== IF Statement ==========")

age = 20

if age >= 18:
    print("You are Eligible to Vote.")

print()


# --------------------------------------------
# 2. IF - ELSE Statement
# --------------------------------------------

# Definition:
# if condition True ho to if block chalega.
# Agar condition False ho to else block chalega.

print("========== IF ELSE Statement ==========")

age = 15

if age >= 18:
    print("You are an Adult.")
else:
    print("You are a Minor.")

print()


# --------------------------------------------
# 3. IF - ELIF - ELSE Statement
# --------------------------------------------

# Definition:
# Jab multiple conditions check karni ho tab
# elif use karte hain.

print("========== IF ELIF ELSE ==========")

marks = 75

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 50:
    print("Grade C")

else:
    print("Fail")

print()


# --------------------------------------------
# 4. Nested IF
# --------------------------------------------

# Definition:
# Jab ek if ke andar doosra if likhte hain
# use Nested IF kehte hain.

print("========== Nested IF ==========")

age = 20
has_id = True

if age >= 18:

    if has_id:
        print("Entry Allowed")

    else:
        print("ID Required")

else:
    print("Age Less Than 18")

print()


# --------------------------------------------
# 5. Using AND Operator
# --------------------------------------------

print("========== AND Operator ==========")

age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry Allowed")
else:
    print("Entry Not Allowed")

print()


# --------------------------------------------
# 6. Ternary Operator
# --------------------------------------------

# Definition:
# One Line IF ELSE

print("========== Ternary Operator ==========")

age = 20

status = "Adult" if age >= 18 else "Minor"

print(status)

print()


# --------------------------------------------
# 7. Student Example
# --------------------------------------------

print("========== Student Example ==========")

age = int(input("Enter Your Age : "))

if age >= 18:
    print("Congratulations!")
    print("You Can Vote.")

else:
    print("Sorry!")
    print("You Cannot Vote.")

print()


# --------------------------------------------
# 8. Grade Example
# --------------------------------------------

print("========== Grade Example ==========")

marks = int(input("Enter Your Marks : "))

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 50:
    print("Grade C")

else:
    print("Fail")

print()

print("Program Finished Successfully.")