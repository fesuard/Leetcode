# https://leetcode.com/problems/count-items-matching-a-rule/description/
# Count Items Matching a Rule
# You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item.
# You are also given a rule represented by two strings, ruleKey and ruleValue.
# The ith item is said to match the rule if one of the following is true:
# ruleKey == "type" and ruleValue == typei.
# ruleKey == "color" and ruleValue == colori.
# ruleKey == "name" and ruleValue == namei.
# Return the number of items that match the given rule.
from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0

        for item in items:
            if ruleKey == "type" and item[0] == ruleValue:
                count += 1
            elif ruleKey == "color" and item[1] == ruleValue:
                count += 1
            elif ruleKey == "name" and item[2] == ruleValue:
                count += 1
        return count


class Solution1:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        dic = {'type': 0, 'color': 1, 'name': 2}
        count = 0
        for item in items:
            if item[dic[ruleKey]] == ruleValue:
                count += 1
        return count

