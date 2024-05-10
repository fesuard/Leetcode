https://leetcode.com/problems/truncate-sentence/description/
Truncate Sentence
A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each of the words consists of only uppercase and lowercase English letters (no punctuation).

For example, "Hello World", "HELLO", and "hello world hello world" are all sentences.
You are given a sentence s​​​​​​ and an integer k​​​​​​. You want to truncate s​​​​​​ such that it contains only the first k​​​​​​ words. Return s​​​​​​ after truncating it.

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        idx = []
        for index, char in enumerate(s):
            if char == " ":
                idx.append(index)
        if k > len(idx): return s
        return s[:idx[k-1]]

    
            
