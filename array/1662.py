https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/description/
Check If Two String Arrays are Equivalent
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        str1 = ""
        str2 = ""
        for elem in word1:
            str1 += elem
        for elem in word2:
            str2 += elem
        return str1 == str2
