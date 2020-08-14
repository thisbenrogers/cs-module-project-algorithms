'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

from collections import deque

def sliding_window_max(nums, k):
    # * using deque() solution
    # *     deque() stores indexes of values in each window, maintining 
    # *     a decreasing order so that the max of each window can easily
    # *     be found at the front of the 'qu'
    # * 
    # *     the while loops are removing the smaller items from the window view
    # * 

    n = len(nums)
    qu = deque()
    arr = [] * (len(nums) - k)

    for i in range(k):
        while qu and nums[i] >= nums[qu[-1]]:
            qu.pop()
        qu.append(i)

    for i in range(k, n):
        arr.append(nums[qu[0]])
        while qu and qu[0] <= (i - k):
            qu.popleft()
        while qu and nums[i] >= nums[qu[-1]]:
            qu.pop()
        qu.append(i)
    arr.append(nums[qu[0]])
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
