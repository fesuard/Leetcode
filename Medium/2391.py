# https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/description
# You are given a 0-indexed array of strings garbage where garbage[i] represents the assortment of garbage at the ith house.
# garbage[i] consists only of the characters 'M', 'P' and 'G' representing one unit of metal, paper and glass garbage respectively.
# Picking up one unit of any type of garbage takes 1 minute.
# You are also given a 0-indexed integer array travel where travel[i] is the number of minutes needed to go from house i to house
# i + 1. There are three garbage trucks in the city, each responsible for picking up one type of garbage. Each garbage truck starts
# at house 0 and must visit each house in order; however, they do not need to visit every house. Only one garbage truck may be used 
# at any given moment. While one truck is driving or picking up garbage, the other two trucks cannot do anything.
# Return the minimum number of minutes needed to pick up all the garbage.


# First we find the max index of each of the three garbage types, we add the length of each string then we add the travel sum at
# based on the max index
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        res = 0
        last_position = {'P': 0, 'G': 0, 'M': 0}
        
        for i in range(len(garbage)):
            res += len(garbage[i])
            for g in garbage[i]:
                last_position[g] = i

        for index in last_position.values():
            res += sum(travel[:index])

        return res
