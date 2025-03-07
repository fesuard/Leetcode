# https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/description
# You are given an n × n grid and a robot starting at startPos = [row, col].
# The robot follows a string s of instructions ('L', 'R', 'U', 'D') and executes
# them one by one. From each index i in s, the robot moves until it either:
#   Moves out of bounds.
#   Reaches the end of the string.
# Return an array where each element answer[i] is the number of moves the robot 
# can make if it starts executing from the i-th instruction.


class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        a, b = startPos[0], startPos[1]
        res = []

        for i in range(len(s)):
            moves = 0
            a, b = startPos[0], startPos[1]
            for j in range(i, len(s)):
                if s[j] == "U":
                    a -= 1
                    if a in range(n):
                        moves += 1
                    else:
                        break
                
                if s[j] == "D":
                    a += 1
                    if a in range(n):
                        moves += 1
                    else:
                        break
                
                if s[j] == "L":
                    b -= 1
                    if b in range(n):
                        moves += 1
                    else:
                        break
                
                if s[j] == "R":
                    b += 1
                    if b in range(n):
                        moves += 1
                    else:
                        break
            
            res.append(moves)

        return res
