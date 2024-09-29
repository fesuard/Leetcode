# https://leetcode.com/problems/two-out-of-three/description/
# Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all
# the values that are present in at least two out of the three arrays.
# You may return the values in any order.
from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        res = []
        nums_total = [nums1, nums2, nums3]
        for lst in nums_total:
            for num in set(lst):
                if ((num in nums1 and num in nums2) or (num in nums1 and num in nums3) or
                        (num in nums2 and num in nums3)):
                    res.append(num)
        return list(set(res))
