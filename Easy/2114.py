# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/description/
# Maximum Number of Words Found in Sentences
# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
# You are given an array of strings sentences, where each sentences[i] represents a single sentence.
# Return the maximum number of words that appear in a single sentence.
from typing import List


# counting spaces
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = []
        for sentence in sentences:
            count = sentence.count(" ")
            res.append(count+1)
        return max(res)


# using split
class Solution1:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res_lst = []
        for sentence in sentences:
            res_lst.append(len(sentence.split()))
        return max(res_lst)