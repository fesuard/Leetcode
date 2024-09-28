https://leetcode.com/problems/sort-the-people/description/
Sort the People
You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        final_list = []
        tuple_list = zip(names, heights)
        sorted_tuple_list = sorted(tuple_list, key=lambda x: x[1], reverse=True)
        for elem in sorted_tuple_list:
            final_list.append(elem[0])
        return final_list     
   
