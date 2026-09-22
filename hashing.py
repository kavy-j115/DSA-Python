"""
Hashing: When counting frequencies in an array the worst-case time complexity can be O(q * n), where q is the number of queries and n is the size of the array. To solve that problem, we create a hash array, which is a precomputation for an array that stores the frequency for each element. When a query is passed, it directly fetches that frequency of the element from hash array instead of looping through the array every time a query is input. This reduces the time complexity to O(q + n), q is the number of query inputs, O(q) and n is the size of the array, and O(n) is the time taken for the precomputation. 

"""

#Number Hashing

# def get_array(size):

#     array = []
#     hash = [0] * 13

#     for i in range(size):
#         num = int(input("Enter a number: "))
#         array.append(num)
#         precomputation(num, hash)

#     return hash

# def precomputation(num, hash):

#     hash[num]+=1

#     return 

# def main():
#     size = int(input("Enter number of elements: "))

#     hash = get_array(size)
#     while True:
#         number = int(input("Enter number to count: "))

#         if 0<= number < len(hash):
#             print(hash[number])
#         else:
#             print("number not in list")

#         choice = input("choice: ")

#         if choice == 'n':
#             break

# if  __name__ == "__main__":
#     main()    

#Character Hashing

# def get_string():
#     string = input("Enter a string: ").strip().lower()

#     return string

# def hashing(freq, string):

#     for character in string:
#         index = ord(character)-ord('a')
#         freq[index] += 1

#     return freq

# def search_frequency(freq, search_index):
#     if freq[search_index] > 0:
#         print(freq[search_index])
#     else:
#         print("character not in string.")

# def main():
#     input_string = get_string()
    
#     freq = hashing([0] * 26, input_string)

#     count = int(input("How many characters do you want to count?"))

#     while count>0:
#         search_char = input("Enter character to count: ")
#         search_index = ord(search_char ) - ord('a')
#         search_frequency(freq, search_index)

#         count -= 1

# if  __name__ == "__main__":
#     main() 


"""
Mapping is more efficient for hashing since it does use extra memory for numbers or characters are not present. In python 'map()' is a function than performs an operation to every element of an iterable. While in C++ it refers to a data-structure that stores key-value pairs. For mapping in python we use 'dictionaries'. Time complexity: 

"""

#Find highest and lowest frequencies

def get_input():

    string = input("Enter your string: ")

    return string

def precomputation(input_string):
    
    frequencies = {}
    for char in input_string:
        frequencies[char] = frequencies.get(char, 0)+1

    return frequencies

def search_frequency(frequencies, search_key):

    if search_key in frequencies:
        frequency = frequencies[search_key]
        print(f"{search_key}: {frequency}")
    else:
        print("Not exists")

def main():
    input_string = get_input()

    freq = precomputation(input_string)

    count = int(input("How many characters do you want to count?"))
    while count>0:
        search_key = input("Enter character to count: ")
        search_frequency(freq, search_key)

        count -= 1

if  __name__ == "__main__":
    main() 

   
