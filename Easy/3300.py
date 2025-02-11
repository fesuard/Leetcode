# https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/description
# You are given an integer array nums.
# You replace each element in nums with the sum of its digits.
# Return the minimum element in nums after all replacements.


# In place solution 
class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = sum(int(num) for num in str(nums[i]))

        return min(nums)


# Using a map function with a lambda expression
class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min(map(lambda x: sum(int(n) for n in str(x)), nums))
