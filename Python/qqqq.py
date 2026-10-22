# Two Sum

nums = [3, 2, 4]
target = 6

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])
            break






nums=[3,2,4]
target=6


for i in range(len(nums)):
    for j in range ( i + 1 , len(nums)):
        if nums [i] + nums [j] == target:
            print ([i,j])
            break


















# s = input("Enter a string: ")

# s = s.lower()

# clean = ""

# for ch in s:
#     if ch.isalnum():
#         clean += ch

# if clean == clean[::-1]:
#     print(True)
# else:
#     print(False)



s= input ("enter the string ")

s= s.lower()

clean = ""

for ch in s:
    if ch.isalnum():
        clean +=ch


if clean == clean[::-1]:
    print (True)
else :
    print (False)    























# prices = [7, 1, 5, 3, 6, 4]

# min_price = prices[0]
# profit = 0

# for price in prices:
#     if price < min_price:
#         min_price = price
#     elif price - min_price > profit:
#         profit = price - min_price

# print(profit)    





































