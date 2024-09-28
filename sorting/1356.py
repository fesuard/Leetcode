https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/description/
Sort Integers by The Number of 1 Bits
You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.

Return the array after sorting it.

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (str(bin(x)).count('1'),x))

Method without using bin:
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        binary_list = []
        final_list =[]
        for elem in arr:
            binary_elem = ""
            while elem >= 1:
                if elem % 2 == 0:
                    binary_elem = "0" + binary_elem
                    elem = elem // 2
                else:
                    binary_elem = "1" + binary_elem
                    elem = elem // 2
            binary_list.append(binary_elem)
        pair_elem = list(zip(arr, binary_list))
        for i in range(len(pair_elem)-1):
            for j in range(0, len(pair_elem)-i-1):
                if pair_elem[j][1].count('1') > pair_elem[j+1][1].count('1'):
                    pair_elem[j], pair_elem[j+1] = pair_elem[j+1], pair_elem[j]
                if pair_elem[j][1].count('1') == pair_elem[j+1][1].count('1') and pair_elem[j][0] > pair_elem[j+1][0]:
                    pair_elem[j], pair_elem[j + 1] = pair_elem[j + 1], pair_elem[j]
        for elem in pair_elem:
            final_list.append(elem[0])
        return final_list
