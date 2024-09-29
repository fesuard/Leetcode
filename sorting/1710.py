# https://leetcode.com/problems/maximum-units-on-a-truck/description/
# You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes,
# where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:
# numberOfBoxesi is the number of boxes of type i.
# numberOfUnitsPerBoxi is the number of units in each box of the type i.
# You are also given an integer truckSize, which is the maximum number of boxes that can be put on
# the truck. You can choose any boxes to put on the truck as long as the number of boxes does not
# exceed truckSize. Return the maximum total number of units that can be put on the truck.
from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        max_sum = 0
        res = 0
        sorted_boxes = sorted(boxTypes, key=lambda x: -x[1])
        for bt in sorted_boxes:
            if bt[0] + max_sum <= truckSize:
                max_sum += bt[0]
                res += bt[0] * bt[1]
            else:
                res += (truckSize-max_sum) * bt[1]
                break
        return res
