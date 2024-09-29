# https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/
# You are given a 0-indexed integer array nums. In one operation, you may do the following:
#     Choose two integers in nums that are equal.
#     Remove both integers from nums, forming a pair.
# The operation is done on nums as many times as possible.
# Return a 0-indexed integer array answer of size 2 where answer[0] is the number of pairs that
# are formed and answer[1] is the number of leftover integers in nums after doing the operation as many times as possible.
from typing import List


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count_dic = {}
        pairs = 0
        for num in nums:
            count_dic[num] = count_dic.get(num, 0) + 1
        for value in count_dic.values():
            if value > 1:
                pairs += value // 2
        leftover = len(nums) - (pairs * 2)
        return [pairs, leftover]
