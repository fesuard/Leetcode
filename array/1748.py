https://leetcode.com/problems/sum-of-unique-elements/description/
You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.
Return the sum of all the unique elements of nums.

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        res = []
        for num in nums:
            if nums.count(num) == 1:
                res.append(num)
        return sum(res)

# using dictionary:
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        res = {}
        sum_res = 0
        for num in nums:
            res[num] = res.get(num, 0) + 1
        for key, value in res.items():
            if value == 1:
                sum_res += key
        return sum_res
