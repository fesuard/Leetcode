# https://leetcode.com/problems/summary-ranges/descriptionYou are given a sorted unique integer array nums.
# A range [a,b] is the set of all integers from a to b (inclusive). Return the smallest sorted list of ranges 
# that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of 
# the ranges, and there is no integer x such that x is in one of the ranges but not in nums. Each range [a,b]
# in the list should be output as: 
# "a->b" if a != b
# "a" if a == b


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        res = []
        i = j = 0

        while i < n and j < n:
            if j + 1 < n and nums[j] + 1 == nums[j+1]:
                j += 1
            else:
                if nums[i] == nums[j]:
                    res.append(str(nums[j]))
                    i += 1
                    j += 1
                else:
                    res.append(f'{nums[i]}->{nums[j]}')
                    j += 1
                    i = j
                    
        return res
