# https://leetcode.com/problems/di-string-match/description
# A permutation perm of n + 1 integers of all the integers in the range [0, n] can be 
# represented as a string s of length n where:
#   s[i] == 'I' if perm[i] < perm[i + 1], and
#   s[i] == 'D' if perm[i] > perm[i + 1].
# Given a string s, reconstruct the permutation perm and return it. If there are multiple
# valid permutations perm, return any of them.


# Since the elements are from 0 to n - 1, when we have an "I", we will add the minimum
# element (starting with 0), and then we add 1 to the minimum. When we have "D", we add
# the max element (starting with n), and then we subtract 1. Lastly, for the last element
# we add at the end either min or max since at that point min == max.
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        min_val = 0
        max_val = len(s)
        res = []

        for char in s:
            if char == "I":
                res.append(min_val)
                min_val += 1
            else:
                res.append(max_val)
                max_val -= 1
        
        res.append(min_val)

        return res
      
