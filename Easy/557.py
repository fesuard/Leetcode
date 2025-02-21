# https://leetcode.com/problems/reverse-words-in-a-string-iii/description
# Given a string s, reverse the order of characters in each word within a sentence 
# while still preserving whitespace and initial word order.


class Solution:
    def reverseWords(self, s: str) -> str:
        word_lst = s.split()

        for i in range(len(word_lst)):
            word_lst[i] = word_lst[i][::-1]

        return " ".join(word_lst)
