https://leetcode.com/problems/find-common-elements-between-two-arrays/description/
Find Common Elements Between Two Arrays
You are given two 0-indexed integer arrays nums1 and nums2 of sizes n and m, respectively.

Consider calculating the following values:

The number of indices i such that 0 <= i < n and nums1[i] occurs at least once in nums2.
The number of indices i such that 0 <= i < m and nums2[i] occurs at least once in nums1.
Return an integer array answer of size 2 containing the two values in the above order.

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = 0
        count2 = 0
        for n in nums1:
            if n in nums2:
                count1 += 1
        for n in nums2:
            if n in nums1:
                count2 += 1
        return [count1, count2]
