# https://leetcode.com/problems/snake-in-matrix/description
# There is a snake in an n x n matrix grid and can move in four possible directions. Each cell in the grid
# is identified by the position: grid[i][j] = (i * n) + j. The snake starts at cell 0 and follows a sequence
# of commands. You are given an integer n representing the size of the grid and an array of strings commands
# where each command[i] is either "UP", "RIGHT", "DOWN", and "LEFT". It's guaranteed that the snake will
# remain within the grid boundaries throughout its movement. Return the position of the final cell where the 
# snake ends up after executing commands.


class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        i = 0
        j = 0

        for command in commands:
            if command == "UP":
                i -= 1
            
            elif command == "DOWN":
                i += 1

            elif command == "LEFT":
                j -= 1
            
            elif command == "RIGHT":
                j += 1
            
        return (i * n) + j
      
