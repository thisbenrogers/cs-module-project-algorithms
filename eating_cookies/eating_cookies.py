'''
Input: an integer
Returns: an integer
'''

from itertools import combinations

def eating_cookies(n):
    # * base case(s)
    if n <= 1:
        return 1
    if n == 2:
        return 2


    # * create a list with a length of n
    arr = list(range(0, n-1))

    # * use itertools.combinations to create a list of 2-length tuple subsets
    tup_arr = list(combinations(arr, 2))

    return len(tup_arr)

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
