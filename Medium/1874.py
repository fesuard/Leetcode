# https://leetcode.com/problems/minimize-product-sum-of-two-arrays/description
# Given two arrays nums1 and nums2 of length n, return the minimum product sum if you are allowed 
# to rearrange the order of the elements in nums1.


class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        n = len(nums1)
        nums1.sort()
        nums2.sort()

        for i in range(n):
            res += nums1[i] * nums2[n - i - 1]

        return res
      
