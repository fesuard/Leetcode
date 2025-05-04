# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/description
# You are given a string s consisting only of uppercase English letters. You can apply some operations
# to this string where, in one operation, you can remove any occurrenceof one of the substrings "AB"
# or "CD" from s.Return the minimum possible length of the resulting string that you can obtain.
# Note that the string concatenates after removing the substring and could produce new "AB" or "CD" 
# substrings.


# Stack approach
class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for char in s:
            if not stack:
                stack.append(char)
            
            elif char == "B" and stack[-1] == "A":
                stack.pop()
            
            elif char == "D" and stack[-1] == "C":
                stack.pop()

            else:
                stack.append(char)

        return len(stack)


# Less optimal than the stack approach, we use the index and string slicing
class Solution1:
    def minLength(self, s: str) -> int:
        while "AB" in s or "CD" in s:
            if "AB" in s:
                index = s.find("AB")
                s = s[ :index] + s[index + 2: ]
            
            elif "CD" in s:
                index = s.find("CD")
                s = s[ :index] + s[index + 2: ]

        return len(s)
        
