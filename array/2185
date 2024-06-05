https://leetcode.com/problems/counting-words-with-a-given-prefix/description/
You are given an array of strings words and a string pref.
Return the number of strings in words that contain pref as a prefix.
A prefix of a string s is any leading contiguous substring of s.

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = []
        for word in words:
            if len(word) >= len(pref) and all(word[i] == pref[i] for i in range(len(pref))):
                res.append(word)
        return len(res)
