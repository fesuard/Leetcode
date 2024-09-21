https://leetcode.com/problems/find-maximum-number-of-string-pairs/description/
You are given a 0-indexed array words consisting of distinct strings.
The string words[i] can be paired with the string words[j] if:
    The string words[i] is equal to the reversed string of words[j].
    0 <= i < j < words.length.
Return the maximum number of pairs that can be formed from the array words.
Note that each string can belong in at most one pair.

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        res = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[i] == words[j][::-1]:
                    res += 1
        return res

#method using set:
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        res = 0
        strings = set()
        for word in words:
            if word in strings:
                res += 1
            else:
                strings.add(word[::-1])
        return res
