from array import array

# initialized array
prime_number = array('i', [2, 3, 5, 7, 13, 17])

# inserted elements in array
prime_number.insert(0, 1)  # time complexity : O(n)
prime_number.insert(5, 11)  # time complexity : O(n)
prime_number.append(19)  # time complexity : O(1)

# print prime_number array
print(f'after inserted elements: {prime_number}')


# traversal operation in prime_number array
def prime_number_traversal(arr):
    i = 0  # time complexity : O(1)
    for element in arr:  # time complexity : O(n)
        print(f'index[{i}]: {element}')  # time complexity : O(1)
        i += 1  # time complexity : O(1)


prime_number_traversal(prime_number)


# accessing elements in prime_number array
def access(arr, index):
    if index >= len(arr):                            # time complexity : O(1)
        return f'sorry this is out of index'         # time complexity : O(1)
    return f'value of index[{index}]: {arr[index]}'  # time complexity : O(1)


result = access(prime_number, 4)
print(result)


# search element in prime_number array
def search_in_prime_number(arr, value):
    for element in arr:                                 # time complexity : O(n)
        if element == value:                            # time complexity : O(1)
            return f'{value} is exist in array'         # time complexity : O(1)
    return f'sorry {value} is not exist in array'       # time complexity : O(1)


result = search_in_prime_number(prime_number, '13')
print(result)

# delete element from prime_number array
prime_number.remove(1)          # time complexity : O(n)
prime_number.remove(11)         # time complexity : O(n)
prime_number.pop()              # time complexity : O(1)
print(f'after deleted elements: {prime_number}')
