# https://leetcode.com/problems/number-of-employees-who-met-the-target/description/
# Number of Employees Who Met the Target
# There are n employees in a company, numbered from 0 to n - 1. Each employee i has worked for hours[i] hours
# in the company. The company requires each employee to work for at least target hours.
# You are given a 0-indexed array of non-negative integers hours of length n and a non-negative integer target.
# Return the integer denoting the number of employees who worked at least target hours.
from typing import List


# using filter
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        target_employee = filter(lambda x: x >= target, hours)
        return len(list(target_employee))


# using generator
class Solution1:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return sum(hour >= target for hour in hours)
