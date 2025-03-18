# https://leetcode.com/problems/rings-and-rods/description
# Given a string rings representing n rings placed on ten rods (labeled 0 to 9), 
# determine how many rods have at least one red (R), green (G), and blue (B) ring. 
# Each pair of characters in rings represents a ring's color and the rod it is placed
# on. The goal is to count the number of rods that contain all three colors.


# We first create a dictionary storing the rod numbers as keys, and the colors attached to
# the rods as values. If a color is already added we won't add it again. Lastly we check the 
# lengths of the value lists, and if the length is 3, that meants it has all the 3 colors
# and we increment res.
class Solution:
    def countPoints(self, rings: str) -> int:
        rods_color = defaultdict(list)
        res = 0

        for i in range(1, len(rings), 2):
            if rings[i - 1] not in rods_color[rings[i]]:
                rods_color[rings[i]].append(rings[i - 1])
        
        for rod in rods_color:
            if len(rods_color[rod]) == 3:
                res += 1

        return res
      
