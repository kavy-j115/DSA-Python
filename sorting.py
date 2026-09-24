from typing import Final
ARRAY:Final = [9,3,4,2,5,1]

"""Common Functions"""

def swap(arr, index_min, index_max):
    
    arr[index_min], arr[index_max] = arr[index_max], arr[index_min]
    return arr

def get_array(n):
    array = []
    for i in range(n):
        element = int(input("Enter a number: "))
        array.append(element)

    return array

#Selection Sort
"""
Find the smallest number in the unsorted portion, swap it with the element at 'start', then increase 'start' recursively.
"""

# def selectionSort(array, start=0):
#     if start>(len(array)-1):
#         return array

#     min_index = start

#     for i in range(start+1, len(array)):
#         if array[i] < array[min_index]:
#             min_index = i

#     swap(array, start, min_index)

#     return selectionSort(array, start+1)

# def selectionIterative(arr):
        
#     for i in range(len(arr)-1): 
#         min_index = i
#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[min_index]:
#                 min_index = j

#         swap(arr, i, min_index)

#     return arr

# def main():
#     size = int(input("Enter size of array: "))

#     array = get_array(size)
#     print("Original Array: {}".format(array))

#     # sorted_array = selectionSort(array)
#     sorted_array = selectionIterative(array)

#     print("Sorted Array: {}".format(sorted_array))

# if __name__ == "__main__":
#     main()

#Bubble Sort
""" 
Checks the next element in each pass and replace them if the next element is smaller than the current index. Puts the largest element in the end fitst and so on.

"""
# def bubbleSort(arr, length):
#     if length==0:
#         return arr
    
#     for i in range(0, length-1):
#         if arr[i] > arr[i+1]:
#             swap(arr, i, i+1)

#     return bubbleSort(arr, length-1)

# def bubbleIterative(arr):

#     for i in range(len(arr)-1):
#         for j in range(len(arr)-1-i):
#             if arr[j] > arr[j+1]:
#                 swap(arr, j, j+1)

#     return arr

# def main():
    # size = int(input("Enter size of array: "))
#     array = ARRAY
#     length=len(array)
#     print(f"Original Array: {array}")

#     arr = bubbleIterative(array)
#     print(f"Sorted Array: {arr}")

# if __name__ == "__main__":
#     main()

def insertionSort(arr):

    for i in range(1, len(arr)):
        key = arr[i]

        j = i - 1

        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j-=1

        arr[j+1] = key

    return arr

def insertionRecursive(arr, i):

    if i >= len(arr):
        return arr

    key = arr[i]
    j = i-1

    while j>=0 and key<arr[j]:
        arr[j+1] = arr[j]
        j-=1
    
    arr[j+1] = key

    return insertionRecursive(arr, i+1)

def main():
    size = int(input("Enter array size: "))
    array = get_array(size)
    print(array)
    insertionSort(array)
    print(array)
    sort = insertionRecursive(array, i=0)
    print(sort)

if __name__ == "__main__":
    main()
        