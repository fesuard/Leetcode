# https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/description
# You are given a string s. Simulate events at each second i:
# If s[i] == 'E', a person enters the waiting room and takes one of the chairs in it.
# If s[i] == 'L', a person leaves the waiting room, freeing up a chair.
# Return the minimum number of chairs needed so that a chair is available for every
# person who enters the waiting room given that it is initially empty.


# We iterate through the characters of s, if the person is entering 'E', we increment
# current, if the person is leaving 'L' we decrement current. And if current is bigger
# than res, we assign current to res.
class Solution:
    def minimumChairs(self, s: str) -> int:
        current = 0
        res = 0

        for char in s:
            if char == 'E':
                current += 1
            else:
                current -= 1
            
            res = max(res, current)
        
        return res
      
