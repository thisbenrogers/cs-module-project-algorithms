'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # sort list in-place
    # compare each value to the next, removing duplicates
    # return any remaining integer,
 
    arr.sort()
    i = 0
    prev = None
    while i < len(arr):
        item = arr[i]
        if item == prev:
            arr.pop(i)
            arr.pop(i - 1)
            i -= 1
        else:
            i += 1
        if i:
            prev = arr[i - 1]
        else:
            prev = None
    return arr[0]




if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")