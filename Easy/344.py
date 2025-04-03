# https://leetcode.com/problems/reverse-string/description\
# Write a function that reverses a string. The input string is given as an array
# of characters s. You must do this by modifying the input array in-place with
# O(1) extra memory.


# Since we have to modify the string in place, we just do a for loop until
# n // 2, the i-th element with the n-i-1-th element.
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)

        for i in range(n // 2):
            s[i], s[n - i - 1] = s[n - i - 1], s[i]
          
