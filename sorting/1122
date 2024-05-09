https://leetcode.com/problems/relative-sort-array/description/
Relative Sort Array
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        final_list = []
        arr1.sort()
        diff_list = []
        for elem in arr2:
            if elem in arr1:
                final_list += [elem] * arr1.count(elem)
        for elem in arr1:
            if elem not in arr2:
                diff_list.append(elem)

        return final_list + diff_list
