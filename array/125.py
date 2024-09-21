# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
# removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric
# characters include letters and numbers.Given a string s, return true if it is a palindrome,
# or false otherwise.

# with 2 indexes
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().strip()
        string = "".join(letter for word in s for letter in word if letter.isalnum())
        i = 0
        n = len(string)-1
        pal = True
        while i < n:
            if string[i] != string[n]:
                pal = False
                break
            i += 1
            n -= 1
        return pal

# with reversing the string:
class Solution1:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().split()
        s1 = "".join(letter for word in s for letter in word if letter.isalnum())
        if s1 == s1[::-1]:
            return True
        return False
