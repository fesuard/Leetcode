https://leetcode.com/problems/shuffle-string/description/
Shuffle String
You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res_lst = [''] * len(indices)
        for i in range(len(indices)):
            res_lst[indices[i]] = s[i]
        return ''.join(res_lst)
