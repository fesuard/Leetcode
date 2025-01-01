# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/description
# You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:
# The 2D array should contain only the elements of the array nums.
# Each row in the 2D array contains distinct integers.
# The number of rows in the 2D array should be minimal.
# Return the resulting array. If there are multiple answers, return any of them.
# Note that the 2D array can have a different number of elements on each row.


class Solution:
    def findMatrix(self, nums):
        matrix = []

        while nums:
            i = 0
            temp = []

            while i < len(nums):
                if nums[i] not in temp:
                    temp.append(nums[i])
                    nums.pop(i)
                
                else:
                    i += 1

            matrix.append(temp)
        
        return matrix
