# https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/description
# You are given a 0-indexed string array words.
# Let's define a boolean function isPrefixAndSuffix that takes two strings, str1 and str2:
# isPrefixAndSuffix(str1, str2) returns true if str1 is both a prefix and a suffix of str2,
# and false otherwise. 
# Return an integer denoting the number of index pairs (i, j) such that i < j, and
# isPrefixAndSuffix(words[i], words[j]) is true.


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1, str2):
            n1 = len(str1)
            if str1 == str2[:n1] and str1 == str2[-n1:]:
                return True
    
        res = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if len(words[i]) <= len(words[j]):
                    if isPrefixAndSuffix(words[i], words[j]):
                        res += 1

        return res
