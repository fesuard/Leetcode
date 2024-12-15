# https://leetcode.com/problems/contains-duplicate/description
# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashm = {}

        for elem in nums:
            hashm[elem] = hashm.get(elem, 0) + 1

        for elem in hashm.values():
            if elem > 1:
                return True
        
        return False
      
