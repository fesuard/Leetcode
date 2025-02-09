# https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/description
# You have an array of floating point numbers averages which is initially empty. You are given an
# array nums of n integers where n is even. You repeat the following procedure n / 2 times:
# Remove the smallest element, minElement, and the largest element maxElement, from nums.
# Add (minElement + maxElement) / 2 to averages.
# Return the minimum element in averages.


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        n = len(nums)
        nums.sort()
        res = float("inf")
        
        for i in range(n // 2):
            num = (nums[i] + nums[n - i - 1]) / 2
            res = min(res, num)

        return res
        
