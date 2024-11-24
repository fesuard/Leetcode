# https://leetcode.com/problems/third-maximum-number/description
# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist,
# return the maximum number.

# using sort
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        arr = list(set(nums))
        arr.sort()
        if len(arr) > 2:
            return arr[-3]
        else:
            return max(nums)


# comparing the biggest 3 elements and returning the third
class Solution1:
    def thirdMax(self, nums: List[int]) -> int:
        arr = list(set(nums))
        if len(arr) > 2:
            first = second = third = float('-inf')

            for elem in arr:
                if elem > first:
                    first, second, third = elem, first, second
                elif elem > second:
                    second, third = elem, second
                elif elem > third:
                    third = elem
            
            return third
        
        else:
            return max(nums)
