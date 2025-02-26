# https://leetcode.com/problems/maximum-odd-binary-number/description
# You are given a binary string s that contains at least one '1'. You have to rearrange the bits in such
# a way that the resulting binary number is the maximum odd binary number that can be created from this 
# combination. Return a string representing the maximum odd binary number that can be created from the 
# given combination.
# Note that the resulting string can have leading zeros.


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        hmap = {'0': 0, '1': 0}

        for num in s:
            hmap[num] += 1

        return '1' * (hmap['1'] - 1) + '0' * hmap['0'] + '1' 
