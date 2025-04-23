# https://leetcode.com/problems/transform-array-by-parity/description
# You are given an integer array nums. Transform nums by performing the following
# operations in the exact order specified:
# Replace each even number with 0.
# Replace each odd numbers with 1.
# Sort the modified array in non-decreasing order.
# Return the resulting array after performing these operations.


# We start by creating an array of [0] times the length of the array, and then
# we iterate through nums, and if the number is odd, we add it as the last index
# in our new array and we decrement index by 1.
class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)   
        index = len(nums) - 1

        for num in nums:
            if num % 2 != 0:
                res[index] = 1
                index -= 1
        
        return res
      
