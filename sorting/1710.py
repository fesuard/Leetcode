https://leetcode.com/problems/maximum-units-on-a-truck/description/
Maximum Units on a Truck

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sorted_list = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        sum = 0
        i=0
        result = 0
        try:
            while sum <= truckSize:
                sum += sorted_list[i][0]
                if sum >= truckSize:
                    sum -= sorted_list[i][0]
                    for j in range(1, sorted_list[i][0]+1):
                        sum += 1
                        if sum <= truckSize:
                            result += 1 * sorted_list[i][1]
                        else:
                            break
                    return result
                result += sorted_list[i][0] * sorted_list[i][1]
                i += 1
        except IndexError:
            return result
    
