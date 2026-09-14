
while True:
    rows = int(input("Ënter number of rows to display: "))

    if rows < 3:
        print("At least 3 rows should be there")
        continue

    break
print()

#Pattern 1: Solid Square

# for row in range(rows):
#     for col in range(rows):
#         print("*", end=" ")
#     print()

#Pattern 2: Right-Angled triangle

# for row in range(1, rows+1):
#     for col in range(row):
#         print("*", end = " ")
#     print()

#Pattern 3: Inverted right angle triangle

# for row in range(rows, 0, -1):
#     for col in range(row):
#         print("*" , end = " ")
#     print() 

#Patter 4: Number triangle

# for row in range(1, rows+1):
#     for col in range(row, 0, -1):
#         print(f"{row - col + 1}", end = "")
#     print()

#Pattern 5: Repeated Number triangle

# for row in range(1, rows+1):
#     for col in range(row):
#         print(row, end = " ")
#     print()

#Pattern 6: Right-Aligned Triangle

# for row in range(1, rows+1):
#     for spaces in range(1, rows-row+1):
#         print(" ", end = " ")

#     for col in range(row):
#         print("*", end = " ")

#     print()

#Pattern 7: Inverted Right-Aligned Triangle

# for row in range(rows, 0, -1):
#     for spaces in range(rows-row):
#         print(" ", end = " ")

#     for col in range(row):
#         print("*", end = " ")

#     print()

#Pattern 8: Pyramid

# for row in range(1, rows+1):
#     for spaces in range(rows-row):
#         print(" ", end = " ")
#     for col in range(2*row - 1):
#         print("*", end = " ")
    
#     print()

#Pattern 9: Inverted Pyramid

# for row in range(rows, 0, -1):

#     for spaces in range(rows-row):
#         print(" ", end = " ")

#     for col in range(2*row - 1):
#         print("*", end = " ")

#     print()

#Pattern 10: Diamond

# for row in range(1, rows):
#     for spaces in range(rows-row):
#         print(" ", end = " ")
#     for col in range(2*row - 1):
#         print("*", end = " ")

#     print()

# for row in range(rows, 0, -1):
#     for spaces in range(rows-row):
#         print(" ", end = " ")

#     for col in range(2*row - 1):
#         print("*", end = " ")

#     print()

#Pattern 11: Number Pyramid

# for row in range(1, rows+1):
#     for spaces in range(rows-row):
#         print(" ", end = " ")

#     for col in range(1, 2*row):
#         print(col, end = " ")

#     print()

#Pattern 11: Repeated Number Pyramid

# for row in range(1, rows+1):
#     for spaces in range(rows-row):
#         print(" ", end = " ")

#     for col in range(1, 2*row):
#         print(row, end = " ")

#     print()

#Pattern 12: Inverted Number Pyramid

# for row in range(rows, 0, -1):
#     for spaces in range(rows-row):
#         print(" ", end = " ")

#     for col in range(1, 2*row):
#         print(col, end = " ")

#    print()

#Pattern 13:
# count=1
# for row in range(1, rows+1):
    
#     for col in range(row):
#         print(count, end = " ")
#         count+=1

#     print()

#Patter 14: 


print()    