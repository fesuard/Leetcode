# https://leetcode.com/problems/finding-3-digit-even-numbers/description/
# You are given an integer array digits, where each element is a digit. The array may contain duplicates.
# You need to find all the unique integers that follow the given requirements:
# The integer consists of the concatenation of three elements from digits in any arbitrary order.
#   The integer does not have leading zeros.
#   The integer is even.
#   For example, if the given digits were [1, 2, 3], integers 132 and 312 follow the requirements.
# Return a sorted array of the unique integers.
from collections import Counter


# We use 3 fors for each pottential digit and check the frequency of each digit to ensure the 
# number can be formed taking into account the duplicates, and if it is, we add it in res.
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = Counter(digits)
        res = []
        
        for i in range(1, 10):
            for j in range(0, 10):
                for k in range(0, 10, 2):
                    if freq[i] > 0 and freq[j] > (i == j) and freq[k] > (i == k) + (j == k):
                        res.append(i * 100 + j * 10 + k)

        return res


# We iterate through each even number from 100 to 998, we split the number into digits,
# we do a separate frequency counter for the digits, and we check if the frequency of 
# the digits allows us to form the number.
class Solution1:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = Counter(digits)
        res = []

        for num in range(100, 999, 2):
            new_digits = [num // 100, num // 10 % 10, num % 10]
            digits_count = Counter(new_digits)

            if all(freq[d] >= digits_count[d] for d in new_digits):
                res.append(num)

        return res
