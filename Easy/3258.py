# https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/description
# You are given a binary string s and an integer k.
# A binary string satisfies the k-constraint if either of the following conditions holds:
#   The number of 0's in the string is at most k.
#   The number of 1's in the string is at most k.
# Return an integer denoting the number of substrings of s that satisfy the k-constraint.


# Brute-force approach, we use 2 fors, at each step we add the 0's and 1's to their 
# respective counter variable, and check if either of them are less than or equal to k
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        res = 0

        for i in range(len(s)):
            count_0, count_1 = 0, 0
            for j in range(i, len(s)):
                if s[j] == '0':
                    count_0 += 1
                elif s[j] == '1':
                    count_1 += 1
                
                if count_0 <= k or count_1 <= k:
                    res += 1
        
        return res
  
