# https://leetcode.com/problems/find-the-original-array-of-prefix-xor/description
# You are given an integer array pref of size n. Find and return the array arr of size
# n that satisfies:
# pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].
# Note that ^ denotes the bitwise-xor operation.
# It can be proven that the answer is unique.


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = [pref[0]]  

        for i in range(1, len(pref)):
            xor = pref[i] ^ pref[i - 1]
            res.append(xor)

        return res
      
