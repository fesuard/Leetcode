# https://leetcode.com/problems/find-the-number-of-good-pairs-i/description
# You are given 2 integer arrays nums1 and nums2 of lengths n and m respectively. You are also given a positive integer k.
# A pair (i, j) is called good if nums1[i] is divisible by nums2[j] * k (0 <= i <= n - 1, 0 <= j <= m - 1).
# Return the total number of good pairs.


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res = 0
        
        for num1 in nums1:
            for num2 in nums2:
                if num1 % (num2 * k) == 0:
                    res += 1

        return res
      
