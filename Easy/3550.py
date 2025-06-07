# https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/description
# You are given an integer array nums.
# Return the smallest index i such that the sum of the digits of nums[i] is equal to i.
# If no such index exists, return -1.


# We iterate through the index and element of our integer array, and when we find an index
# that is equal to the element's digit sum, we return it
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            sum_digits = sum(int(d) for d in str(num))
            if i == sum_digits:
                return i

        return -1
