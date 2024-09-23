# https://leetcode.com/problems/kth-distinct-string-in-an-array/description/
# A distinct string is a string that is present only once in an array.
# Given an array of strings arr, and an integer k, return the kth distinct string present in arr.
# If there are fewer than k distinct strings, return an empty string "".
# Note that the strings are considered in the order in which they appear in the array.
from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        str_dic = {}
        for string in arr:
            str_dic[string] = str_dic.get(string, 0) + 1
        str_list = []
        for key, value in str_dic.items():
            if value == 1:
                str_list.append(key)
        if len(str_list) >= k:
            return str_list[k-1]
        else:
            return ""
