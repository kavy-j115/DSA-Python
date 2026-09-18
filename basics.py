"""

Working with mathematical problems to work on logic building skills.

"""
import math

# Count digits

number = int(input("Ënter a number: "))

""" Approacg one: """

# count = 0
# temp_number = number

# while int(temp_number) > 0:
#     count += 1
#     temp_number /= 10

# print("Number of digits in {} = {}".format(number, count))

""" Approach two: """

# count = int(math.log10(number) + 1)

# print(count)

#Reverse Digits

# reverse_num = 0 
# num = number
# while num>0:
#     last_digit = num % 10
#     reverse_num = (reverse_num*10) + last_digit
#     num //= 10
# print(reverse_num)

#Palindrome Number

# reverse_num = 0
# temp_num = number

# while temp_num>0:

#     digit = temp_num%10
#     reverse_num = (reverse_num*10) + digit
#     temp_num //= 10

# if number == reverse_num:
#     print("Palindrome.\n")
# else:
#     print("Not Palindrome.\n")

#Armstrong Number

# temp_num = number
# temp_num2 = number
# count = 0
# sumdigits = 0

# while temp_num > 0:
#     digit = temp_num%10
#     count += 1
#     temp_num//=10

# while number > 0:
#     digit = number%10
#     sumdigits = sumdigits + (digit**count)
#     number = number//10

# if temp_num2 == sumdigits:
#     print("Armstrong")
# else:
#     print("Not Armstrong")

#Prime Number

count = 0
# divisor = 1

# while divisor < number:

#     if number%divisor == 0:
#         count += 1

#         if count > 1:
#             print("Not Prime")
#             break

#     divisor += 1
# else:
#     print("Prime.")

# if number <= 1:
#     print("Not Prime") 

# else:
#     for i in range(2, int(math.sqrt(number))+1):

#         if number%i == 0:
#             print("Not Prime.")
#             break
#     else:
#         print("Prime.")

#Find all factors

# factors = []
# for i in range(1, int(math.sqrt(number))+1):

#     if number%i == 0:
#         factors.append(i)
#         if number/i != i:
#             factors.append(int(number/i))

# print(sorted(factors))

#Highest common factor

num2 = int(input("Enter another number: "))

"""Brute Force Approach"""
# common_factor = 1

# for i in range(2, min(number, num2)+1):
#     if number%i == 0 and num2%i == 0:
#             common_factor = i

# print("highest common factor: {}".format(common_factor))

"""Euclidean Algorithm"""

# while num2:
#     number, num2 = num2, number%num2
#     print(num2, number)
# print("highest common factor: {}".format(number))