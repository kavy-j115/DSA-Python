"""
When a function calls itself until a specified condition is met which is the base condition.

When there is no base condition the recursion becomes an infinite recursion and causes stack overflow.

Stack Overflow: When the recursion uses more memory than it was allocated. 

Recursion Tree: Representation of the recursion in a tree form.

Important: Make sure to understand when the work is done; while going up in the stack or coming back down? It is very important.

Backtracking means that the function is executed while returning when the base condition of a recursion is satisfied.

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

# if __name__ == "__main__":
#     main()