# ====================================================
# FOR LOOP & RANGE() - COMPLETE PROGRAM
# ====================================================

# ----------------------------------------------------
# 1. Basic FOR Loop
# ----------------------------------------------------

# Definition:
# for loop sequence ke har item par ek-ek
# karke execute hota hai.

print("========== BASIC FOR LOOP ==========")

for i in range(5):

    print(i)

print()


# ----------------------------------------------------
# 2. range(stop)
# ----------------------------------------------------

# Definition:
# range(stop) 0 se start hota hai aur
# stop value se pehle ruk jata hai.

print("========== RANGE(STOP) ==========")

for i in range(5):

    print(i)

print()


# ----------------------------------------------------
# 3. range(start, stop)
# ----------------------------------------------------

print("========== RANGE(START, STOP) ==========")

for i in range(2,7):

    print(i)

print()


# ----------------------------------------------------
# 4. range(start, stop, step)
# ----------------------------------------------------

print("========== RANGE WITH STEP ==========")

for i in range(0,11,2):

    print(i)

print()


# ----------------------------------------------------
# 5. Negative Step
# ----------------------------------------------------

print("========== COUNTDOWN ==========")

for i in range(10,0,-1):

    print(i)

print()


# ----------------------------------------------------
# 6. String Iteration
# ----------------------------------------------------

# Definition:
# String ke har character ko access karna.

print("========== STRING ITERATION ==========")

name = "Python"

for letter in name:

    print(letter)

print()


# ----------------------------------------------------
# 7. Sum Example
# ----------------------------------------------------

# Definition:
# Accumulator Variable result collect karta hai.

print("========== SUM ==========")

total = 0

for num in range(1,11):

    total = total + num

print("Total =", total)

print()


# ----------------------------------------------------
# 8. Even Odd Example
# ----------------------------------------------------

print("========== EVEN ODD ==========")

for num in range(1,11):

    if num % 2 == 0:

        print(num,"Even")

    else:

        print(num,"Odd")

print()


# ----------------------------------------------------
# 9. Nested FOR Loop
# ----------------------------------------------------

# Definition:
# Loop ke andar loop.

print("========== NESTED FOR LOOP ==========")

for i in range(1,4):

    for j in range(1,4):

        print(i,"x",j,"=",i*j)

print()


# ----------------------------------------------------
# 10. Table Program
# ----------------------------------------------------

print("========== TABLE PROGRAM ==========")

number = int(input("Enter Number : "))

for i in range(1,11):

    result = number*i

    if result % 2 ==0:

        print(number,"x",i,"=",result,"Even")

    else:

        print(number,"x",i,"=",result,"Odd")

print()


# ----------------------------------------------------
# 11. Vowel Counter
# ----------------------------------------------------

print("========== VOWEL COUNTER ==========")

word = input("Enter Word : ")

vowels = "aeiouAEIOU"

count = 0

for letter in word:

    if letter in vowels:

        count +=1

print("Total Vowels =",count)

print()

print("Program Finished Successfully.")