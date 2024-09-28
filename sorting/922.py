https://leetcode.com/problems/sort-array-by-parity-ii/description/
Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

Return any answer array that satisfies this condition.

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        i = 0
        j = 1
        while nums:
            n = nums.pop()
            if n % 2 == 0:
                res[i] = n
                i += 2
            else:
                res[j] = n
                j += 2

        return res
