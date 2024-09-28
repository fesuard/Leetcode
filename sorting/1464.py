https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description/
Maximum Product of Two Elements in an Array
Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        result = (nums[-1]-1)*(nums[-2]-1)
        return result    
