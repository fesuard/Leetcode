# https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/description/
# The value of an alphanumeric string can be defined as:
#     The numeric representation of the string in base 10, if it comprises of digits only.
#     The length of the string, otherwise.
# Given an array strs of alphanumeric strings, return the maximum value of any string in strs.
import re
from typing import List


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        re_pattern = r'^\d+$'
        res = []
        for elem in strs:
            if bool(re.fullmatch(re_pattern, elem)):
                res.append(int(elem))
            else:
                res.append(len(elem))
        return max(res)
