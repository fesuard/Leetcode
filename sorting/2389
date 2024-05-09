https://leetcode.com/problems/longest-subsequence-with-limited-sum/description/
Longest Subsequence With Limited Sum
You are given an integer array nums of length n, and an integer array queries of length m.

Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums such that the sum of its elements is less than or equal to queries[i].

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        m = len(queries)
        answer = [0] * m
        indexes = sorted(range(m), key=lambda i: queries[i])
        s = j = 0
        for index in indexes:
            while j < len(nums) and s+nums[j] <= queries[index]:
                s += nums[j]
                j += 1
            answer[index] = j
        return answer
