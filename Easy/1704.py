# https://leetcode.com/problems/determine-if-string-halves-are-alike/description
# You are given a string s of even length. Split this string into two halves of 
# equal lengths, and let a be the first half and b be the second half.
# Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u',
# 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.
# Return true if a and b are alike. Otherwise, return false.


# We iterate through the indexes in the first half, we also check n - i - 1, for the
# second half. If a vowel is in the first half we increment balance by 1, if a vowel
# is in the second half we decrement balance by 1. If balance is 0, we return True.
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        balance = 0
        vowels = set("aeiouAEIOU")

        for i in range(n // 2):
            if s[i] in vowels:
                balance += 1
            
            if s[n - i - 1] in vowels:
                balance -= 1
        
        return balance == 0
