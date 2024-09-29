# https://leetcode.com/problems/merge-similar-items/description/
# You are given two 2D integer arrays, items1 and items2, representing two sets of items. Each array items has the
# following properties:
# items[i] = [valuei, weighti] where valuei represents the value and weighti represents the weight of the ith item.
# The value of each item in items is unique. Return a 2D integer array ret where ret[i] = [valuei, weighti], with
# weighti being the sum of weights of all items with value valuei. Note: ret should be returned in ascending order
# by value.
from typing import List


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        all_items = items1 + items2
        dic_items = {}
        for key, value in all_items:
            dic_items[key] = dic_items.get(key, 0) + value
        return sorted(list(dic_items.items()))
