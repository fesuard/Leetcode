https://leetcode.com/problems/divide-array-into-equal-pairs/description/
You are given an integer array nums consisting of 2 * n integers.
You need to divide nums into n pairs such that:
    Each element belongs to exactly one pair.
    The elements present in a pair are equal.
Return true if nums can be divided into n pairs, otherwise return false.

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        res = True
        num_count = {}
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
        for value in num_count.values():
            if value % 2 != 0:
                return False
        return res
