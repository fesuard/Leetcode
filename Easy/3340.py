# https://leetcode.com/problems/check-balanced-string/description
# You are given a string num consisting of only digits. A string of digits is called balanced if
# the sum of the digits at even indices is equal to the sum of digits at odd indices. Return true
# if num is balanced, otherwise return false.


# iterative solution
class Solution:
    def isBalanced(self, num: str) -> bool:
        even = 0
        odd = 0
        
        for i in range(len(num)):
            if i % 2 == 0:
                even += int(num[i])
            else:
                odd += int(num[i])

        return even == odd


# Using map and list slicing
class Solution1:
    def isBalanced(self, num: str) -> bool:
        num = list(map(int, num))

        return sum(num[0 : len(num) : 2]) == sum(num[1 : len(num) : 2])
      
