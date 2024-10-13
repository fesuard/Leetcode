# https://leetcode.com/problems/word-pattern/description
# Given a pattern and a string s, find if s follows the same pattern. Here follow means a full match, such that there
# is a bijection between a letter in pattern and a non-empty word in s. Specifically: Each letter in pattern maps to 
# exactly one unique word in s. Each unique word in s maps to exactly one letter in pattern. No two letters map to the
# same word, and no two words map to the same letter.


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()
        pattern_index = []
        s_index = []
        if len(s_list) == len(pattern):
            for i in range(len(pattern)):
                pattern_index.append(pattern.index(pattern[i]))
                s_index.append(s_list.index(s_list[i]))
            return pattern_index == s_index
        return False
