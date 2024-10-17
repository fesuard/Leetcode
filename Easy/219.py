# https://leetcode.com/problems/contains-duplicate-ii/description
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in 
# the array such that nums[i] == nums[j] and abs(i - j) <= k.


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hmap = {}
        for i in range(len(nums)):
            if nums[i] in hmap:
                if abs(i - hmap[nums[i]]) <= k:
                    return True
                else:
                    hmap[nums[i]] = i
            else:
                hmap[nums[i]] = i
        return False
