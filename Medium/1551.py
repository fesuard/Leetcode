# https://leetcode.com/problems/minimum-operations-to-make-array-equal/description
# You have an array arr of length n where arr[i] = (2 * i) + 1 forall valid values
# of i (i.e., 0 <= i < n). In one operation, you canselect two indices x and y where 
# 0 <= x, y < n and subtract 1 from arr[x] and add 1 to arr[y] (i.e., perform arr[x]
# -=1 and arr[y] += 1). The goal is to make all the elements of the array equal.
# Given an integer n, the length of the array, return the minimum number of operations
# needed to make all the elements of arr equal.


# Since we have to make the minimum number of operations, we determine that the target of
# each number of the array is the average of our array. Then we return the difference between 
# each number and the target and divide that by 2.
class Solution:
    def minOperations(self, n: int) -> int:
        arr = [2 * i + 1 for i in range(n)]
        target = sum(arr) / n
        sum_difference = 0

        for elem in arr:
            sum_difference += abs(target - elem)

        return int(f'{sum_difference // 2:.0f}')
      
