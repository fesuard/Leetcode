# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/description/
# Given an array nums of even length n, pair up the elements of nums
# into n / 2 pairs such that:
# Each element of nums is in exactly one pair, and
# The maximum pair sum is minimized.
# Return the minimized maximum pair sum after optimally pairing up the elements.


# We first sort the array, then we pair the elements optimally, by pairing the 
# biggest with the smallest, second biggest with the second smallest and so on
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        nums.sort()

        for i in range(n // 2):
            res = max(res, nums[i] + nums[n - i - 1])
        
        return res
      
