https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            result_num = 0
            for j in range(len(nums)):
                if i != j and nums[j] < nums[i]:
                    result_num += 1
            result.append(result_num)
        return result
