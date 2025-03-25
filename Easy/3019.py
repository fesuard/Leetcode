# https://leetcode.com/problems/number-of-changing-keys/description
# You are given a 0-indexed string s typed by a user. Changing a key is defined as
# using a key different from the last used key. For example, s = "ab" has a change 
# of a key while s = "bBBb" does not have any. Return the number of times the user 
# had to change the key.


# If the length of the list is 1 no keys will be changed so we return 0. If not, 
# we assign the first letter of s to prev, and we start from indice 1 to the last
# element, we compare lowered prev to the lowered current letter, and if they are 
# different, prev will be the current letter, and the result is incremented by 1.
class Solution:
    def countKeyChanges(self, s: str) -> int:
        res = 0
        prev = s[0]
        n = len(s)

        if n == 1:
            return 0
        
        for i in range(1, n):
            if prev.lower() != s[i].lower():
                prev = s[i]
                res += 1
        
        return res
      
