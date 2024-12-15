# https://leetcode.com/problems/missing-number/description
# Given an array nums containing n distinct numbers in the range [0, n], return the only number
# in the range that is missing from the array.


# brute forcing by checking number + 1
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        for elem in nums:
            if elem + 1 in range(0, n + 1) and elem + 1 not in nums:
                return elem + 1
        
        return 0


# Gaussian sum
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)    
        return expected_sum - actual_sum      
