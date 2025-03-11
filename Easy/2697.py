# https://leetcode.com/problems/lexicographically-smallest-palindrome
# Given a lowercase English string s, you can replace characters to make it a palindrome
# withthe fewest operations. If multiple palindromes are possible, return the 
# lexicographically smallest one.


class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s_list = list(s)
        n = len(s_list)

        for i in range(n // 2):
            if s_list[i] != s_list[n - i - 1]:
                if s_list[i] < s_list[n - i - 1]:
                    s_list[n - i - 1] = s_list[i]
                else:
                    s_list[i] = s_list[n - i - 1]
        
        return ''.join(s_list)
