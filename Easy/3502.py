# https://leetcode.com/problems/minimum-cost-to-reach-every-position/description
# You start at position n in a line of n+1 people (0 to n). Each person i in front of you charges cost[i] to swap,
# while swaps with those behind you are free. Return an array answer where answer[i] is the minimum cost to reach 
# position i.


# For each cost, we get the minimum value, and if the current cost is lesser than the previous minimum cost, 
# the minimum cost becomes the current cost.
class Solution:
    def minCosts(self, costs: List[int]) -> List[int]:
        res = []
        swap_cost = costs[0]

        for cost in costs:
            swap_cost = min(swap_cost, cost)
            res.append(swap_cost)

        return res
      
