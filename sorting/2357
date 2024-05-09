https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/description/
Make Array Zero by Subtracting Equal Amounts

You are given a non-negative integer array nums. In one operation, you must:

Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
Subtract x from every positive element in nums.
Return the minimum number of operations to make every element in nums equal to 0.

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        i=0
        nums.sort()
        while max(nums) != 0:
            if nums[i] == 0:
                i += 1
            else:
                nums = [x - nums[i] for x in nums]
                count += 1
                i += 1
        return count
