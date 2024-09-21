https://leetcode.com/problems/count-prefixes-of-a-given-string/description/
You are given a string array words and a string s, where words[i] and s comprise 
only of lowercase English letters.
Return the number of strings in words that are a prefix of s.
A prefix of a string is a substring that occurs at the beginning of the string. 
A substring is a contiguous sequence of characters within a string.

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        res = 0
        for i in range(len(s)):
            if s[:i+1] in words:
                res += words.count(s[:i+1])
        return res
