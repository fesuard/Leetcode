# https://leetcode.com/problems/find-center-of-star-graph/description
# There is an undirected star graph consisting of n nodes labeled from 1 to n. A star
# graph is a graph where there is one center node and exactly n - 1 edges that connect
# the center node with every other node. You are given a 2D integer array edges where 
# each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi.
# Return the center of the given star graph.


# since all the nodes are conected to the center node in a star graph, there is no need
# to compare all the nodes, just the first 2
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0] in edges[1]:
            return edges[0][0]
        
        else:
            return edges[0][1]


# if we were to have to compare between all the nodes
class Solution1:
    def findCenter(self, edges: List[List[int]]) -> int:
        for num in edges[0]:
            root = True
            for i in range(1, len(edges)):
                if num not in edges[i]:
                    root = False
                    break
            if root:
                return num
              
