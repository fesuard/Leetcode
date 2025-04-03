# https://leetcode.com/problems/find-unique-binary-string
# Given an array of strings nums containing n unique binary strings each of length n,
# return a binary string of length n that does not appear in nums. If there are multiple
# answers, you may return any of them.


# We use a brut force approach, we get the first number, we iterate and swap the bits
# and check with each swap if the new swapped num is not in nums
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        num = list(nums[0])
        for i in range(len(nums[0])):
            if num[i] == "0":
                num[i] = "1"
            else:
                num[i] = "0"
            
            if ''.join(num) not in nums:
                return ''.join(num)
                
