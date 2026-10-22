#             Pallindrome program

# text = input ("Enter a string: ")

# if text== text [::-1]:
#     print("the string is a palindrome")
# else:
#     print("the string is not a palindrome")


#               Reverse a string

# text =input ("enter the string:")
# print (text [::-1])


#                Reverse List

# numbers =[1,2,3,4,5,6,7,8,9]
# print (numbers[::-1])


#                 Factorial 

# num = int (input ("Enter the number : "))
# fact =1 

# for i in range (1,num+1):
#     fact= fact*i

# print(fact)


#                Fibonacci series

# num = int (input ("Enter the number :" ))

# a=0
# b=1

# for i in range (num):
#     print (a)
#     c=a+b
#     a=b
#     b=c


#               Prime Number 

# num = int (input("enter the number : "))

# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print ("Not Prime")
#             break
#     else: 
#         print ("Prime")
# else:
#     print ("Not Prime")



#               Armstrong Number
   

# num =  int (input ("enter the number :"))

# temp =num 
# sum = 0

# while temp > 0:
#     digit= temp % 10
#     sum = sum + digit ** 3  
#     temp = temp // 10

# if num == sum:
#     print ("Armstrong number")      

# else :
#     print ("Not Armstrong number")    
