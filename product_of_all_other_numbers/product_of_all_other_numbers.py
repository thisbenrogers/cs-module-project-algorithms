'''
Input: a List of integers
Returns: a List of integers
'''

from functools import reduce
from operator import mul

def product_of_all_other_numbers(arr):
    # Your code here

    # * Initialize empty array to hold return value
    # * loop through array once for each value:
    # *     start a current index pointer at 0
    # *     slice a new value, excluding the current index
    # *     preform math on new list values
    # *     append value to return list
    # * return list

    products = [] * (len(arr) - 1)
    for key, value in enumerate(arr):
        temp = arr[:key] + arr[key + 1:]
        products.append(reduce(mul, temp))
    return products


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
