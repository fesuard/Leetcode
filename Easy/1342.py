# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description
# Given an integer num, return the number of steps to reduce it to zero. In one step, 
# if the current number is even, you have to divide it by 2, otherwise, you have to 
# subtract 1 from it.


# iterative solution
class Solution:
    def numberOfSteps(self, num: int) -> int:
        res = 0

        while num > 0:
            if num % 2 == 0:
                num = num // 2
            else:
                num -= 1

            res += 1

        return res


# recursive solution
class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0

        return 1 + (self.numberOfSteps(num // 2) if num % 2 == 0 else self.numberOfSteps(num - 1))
        
