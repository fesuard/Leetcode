https://leetcode.com/problems/find-common-characters/description/
Given a string array words, return an array of all characters that show up in 
all strings within the words (including duplicates). You may return the answer in any order.

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        if len(words) == 1:
            return [char for char in words[0]]
        words1 = set(words[0])
        for char in words1:
            freq = min(word.count(char) for word in words)
            res += [char] * freq
        return res

                
