https://leetcode.com/problems/ant-on-the-boundary/description/
An ant is on a boundary. It sometimes goes left and sometimes right.
You are given an array of non-zero integers nums. The ant starts reading nums from 
the first element of it to its end. At each step, it moves according to the 
value of the current element:
    If nums[i] < 0, it moves left by -nums[i] units.
    If nums[i] > 0, it moves right by nums[i] units.
Return the number of times the ant returns to the boundary.

class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        position = 0
        count = 0
        for num in nums:
            position += num
            if position == 0:
                count += 1
        return count
