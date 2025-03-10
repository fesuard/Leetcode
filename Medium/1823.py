# https://leetcode.com/problems/find-the-winner-of-the-circular-game/description
# There are n friends that are playing a game. The friends are sitting in a circle and are numbered from 1 to n in clockwise order.
# The rules of the game are as follows:
#   Start at the 1st friend.
#   Count the next k friends in the clockwise direction including the friend you started at. The counting wraps around the circle and
#   may count some friends more than once.
#   The last friend you counted leaves the circle and loses the game.
# If there is still more than one friend in the circle, go back to step 2 starting from the friend immediately clockwise of the friend 
# who just lost and repeat. Else, the last friend in the circle wins the game. Given the number of friends, n, and an integer k, 
# return the winner of the game.


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [i for i in range(1, n + 1)]
        current = 0

        while len(friends) > 1:
            current = (current + k - 1) % len(friends)
            friends.pop(current)

        return friends[0]
