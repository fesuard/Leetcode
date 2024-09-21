https://leetcode.com/problems/points-that-intersect-with-cars/description/
You are given a 0-indexed 2D integer array nums representing the coordinates of the cars parking on a number line. 
For any index i, nums[i] = [starti, endi] 
where starti is the starting point of the ith car and endi is the ending point of the ith car.
Return the number of integer points on the line that are covered with any part of a car.

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        points = set()
        for num in nums:
            for i in range(num[0], num[1]+1):
                points.add(i)
        return len(points)
