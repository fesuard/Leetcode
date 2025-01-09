# https://leetcode.com/problems/counting-words-with-a-given-prefix/description/
# You are given an array of strings words and a string pref.
# Return the number of strings in words that contain pref as a prefix.
# A prefix of a string s is any leading contiguous substring of s.


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0
        size = len(pref)

        for word in words:
            if word[:size] == pref:
                res += 1

        return res
