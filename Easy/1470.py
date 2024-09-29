# https://leetcode.com/problems/shuffle-the-array/description/
# Shuffle the Array
# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        final_list = []
        first_list = nums[:n]
        second_list = nums[n:]
        for i in range(0, n):
            final_list.append(first_list[i])
            final_list.append(second_list[i])
        return final_list
