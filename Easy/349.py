# https://leetcode.com/problems/intersection-of-two-arrays/description/
# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must be unique, and you may return the result in any order.
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        final_list = []
        for elem in nums1:
            if elem in nums2 and elem not in final_list:
                final_list.append(elem)
        return final_list


# Using set:
class Solution1:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
