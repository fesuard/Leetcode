# https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/description
# You are given an array nums, where each number in the array appears either
# once or twice. Return the bitwise XOR of all the numbers that appear twice
# in the array, or 0 if no number appears twice.


# We make a frequency hashmap, and check if the number appears twice, if it does
# we xor the number with the previous value saved in xor_val, then we return xor_val.
class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        hmap = {}
        xor_val = 0

        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1

        for num in hmap:
            if hmap[num] == 2:
                xor_val ^= num

        return xor_val
