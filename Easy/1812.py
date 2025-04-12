# https://leetcode.com/problems/determine-color-of-a-chessboard-square/description
# You are given coordinates, a string that represents the coordinates of a square of the chessboard.
# Below is a chessboard for your reference. Return true if the square is white, and false if the square
# is black. The coordinate will always represent a valid chessboard square. The coordinate will always 
# have the letter first, and the number second.


# We create a dictionary to get the number equivalent of the letters from 'a' to 'h'. If the parity is the
# same for both coordinates, the color is black. If not, the color is white.
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        letter_to_digit = {
            'a': 1,
            'b': 2,
            'c': 3,
            'd': 4,
            'e': 5,
            'f': 6,
            'g': 7,
            'h': 8
        }

        if letter_to_digit[coordinates[0]] % 2 == int(coordinates[1]) % 2:
            return False
        else:
            return True
