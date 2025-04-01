# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/description
# You are given a string s consisting of digits. Perform the following operation 
# repeatedly until the string has exactly two digits:
#   For each pair of consecutive digits in s, starting from the first digit, calculate a
# new digit as the sum of the two digits modulo 10.
#   Replace s with the sequence of newly calculated digits, maintaining the order in which
# they are computed.
# Return true if the final two digits in s are the same; otherwise, return false.


# Brute force approach, while the length of the string is greater than 2, we do a for loop
# in the range len - 1 so that we can add the (current element + the next element) % 10
# to temp. After the for loop we assign to s the string stored in temp. After exiting the
# while loop, we just check if the first and second digits are the same.
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            temp = []
            for i in range(len(s) - 1):
                temp.append(str((int(s[i]) + int(s[i + 1])) % 10))

            s = ''.join(temp)
        
        return s[0] == s[1]
    
