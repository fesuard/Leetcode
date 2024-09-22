# https://leetcode.com/problems/destination-city/description/
# You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi.
# Return the destination city, that is, the city without any path outgoing to another city.
# It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.
from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        departure_cities = []
        destination_cities = []
        for i in range(len(paths)):
            departure_cities.append(paths[i][0])
            destination_cities.append(paths[i][1])
        for city in destination_cities:
            if city not in departure_cities:
                return city
