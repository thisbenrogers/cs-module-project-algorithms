'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    
    return [x for x in arr if x != 0] + [0] * arr.count(0)
    
    
    
    # ? The following returned an error from the test 
    # ? on line 56 of test_moving_zeroes.py
    # ? 
    # ? It only sorted 2 of the zeroes to
    # ? the end of the returned list, two other zeroes
    # ? were left at the beginning
    
    # for key, value in enumerate(arr):
    #     if value == 0:
    #         arr.append(value)
    #         arr.pop(key)
    # return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")