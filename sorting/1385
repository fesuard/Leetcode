https://leetcode.com/problems/find-the-distance-value-between-two-arrays/description/
Find the Distance Value Between Two Arrays
Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res_list = []
        for i in arr1:
            if all((abs(i-j) > d for j in arr2)):
                res_list.append(i)
        return len(res_list)
