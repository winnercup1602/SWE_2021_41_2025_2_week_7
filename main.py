from typing import List

# Return the indices of two integers from the given array "nums" that add up to the specified integer "target”
# Assume that only one possible solution exists, and each array element can only be used once. (cannot be used twice or more)
# You can return the answer in any order.
def twoSum(arr, target):
    for idx in range(len(arr)):
        mini_target = target - arr[idx]
        if mini_target in arr and arr.index(mini_target) != idx:
            return [idx, arr.index(mini_target)]

# print(twoSum([2,7,11,15], 9))
# print(twoSum([3,2,4], 6))
# print(twoSum([3,3], 6))