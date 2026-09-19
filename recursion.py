"""
When a function calls itself until a specified condition is met which is the base condition.

When there is no base condition the recursion becomes an infinite recursion and causes stack overflow.

Stack Overflow: When the recursion uses more memory than it was allocated. 

Recursion Tree: Representation of the recursion in a tree form.

"""

#BASIC RECURSION PROBLEMS

#Problem 1: Print name N times

# def print_name(n, name):
#     #Base Condition
#     if n == 0:
#         return

#     #Function
#     print(name)

#     #Recursion Call
#     print_name(n-1, name)

# def main():
#     name  = input("Enter name: ")
#     n = int(input("How many times do you want to print? "))

#     print_name(n, name)
#     print()

#Problem 2: Print from 1 to N linearly

# def print_count(i, n):

#     if i>n:
#         return

#     print(i)

#     print_count(i+1, n)

# def main():
#     n = int(input("Enter a number: "))

#     print_count(1, n)

#Problem 3: Print from N to 1 linearly

# def print_count(n):

#     if n<1:
#         return

#     print(n)

#     print_count(n-1)

# def main():
#     n = int(input("Enter a number: "))

#     print_count(n)

"""

Important: Make sure to understand when the work is done; while going up in the stack or coming back down? It is very important.

Backtracking means that the function is executed while returning when the base condition of a recursion is satisfied.

"""

#Problem 4: Print from 1 to N linearly using backtracking

# def print_count(n):

#     if n<1:
#         return

#     print_count(n-1)

#     #Executed after returning
#     print(n)

# def main():
#     n = int(input("Enter a number: "))

#     print_count(n)

#Problem 5: Print from N to 1 linearly using backtracking

# def print_count(i, n):

#     if i>n:
#         return

#     print_count(i+1, n)

#     print(i)

# def main():
#     n = int(input("Enter a number: "))

#     print_count(1, n)

#Problem 6: Sum of N Numbers

"""Parametrised Recursion: The result is passed as a parameter for the rcursive call."""

# def summation_parameterized(n, total):
#     if n<1:
#         print(total)
#         return
    
#     summation_parameterized(n-1, total+n)

"""
Functional Recursion:
Each recursive call returns a value to the previous call, and each call combines that returned value with its own value to form the final result while backtracking.
"""

# def summation_functional(n):

#     if n<1:
#         return 0
    
#     return n + summation_functional(n-1)

# def main():
#     n = int(input("Enter number: "))

    
#     print("Using functional recursion")
#     summation_parameterized(n, 0) # Parameterized

#     print("Using parametrised recursion")
#     total = summation_functional(n) # Fucntional
#     print(total)

# if __name__ == "__main__":
#     main()

#Problem 7: Factorial of a number

def parameterized_factorial(n, factorial):

    if n==0:
        print(factorial)
        return

    parameterized_factorial(n-1, factorial*n)

def functional_factorial(n):
    if n==0:
        return 1

    return n*functional_factorial(n-1)

def main():
    num = int(input("Enter the number you want to calculate the factorial for: "))

    print("Parameterized Factorial")
    parameterized_factorial(num, 1)

    print("Functional Factorial")
    factorial = functional_factorial(num)
    print(factorial)

if __name__ == "__main__":
    main()