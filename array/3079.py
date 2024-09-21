https://leetcode.com/problems/find-the-sum-of-encrypted-integers/description/
You are given an integer array nums containing positive integers. We define a function encrypt such 
that encrypt(x) replaces every digit in x with the largest digit in x. For example, encrypt(523) = 555 and encrypt(213) = 333.
Return the sum of encrypted elements.

class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        res = []
        for num in nums:
            num_char = str(num)
            res.append(int(max(num_char) * len(num_char)))
        return sum(res)
