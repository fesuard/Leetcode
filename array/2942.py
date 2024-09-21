https://leetcode.com/problems/find-words-containing-character/description/
Find Words Containing Character
You are given a 0-indexed array of strings words and a character x.

Return an array of indices representing the words that contain the character x.

Note that the returned array may be in any order.

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        final_list = []
        for i in range(len(words)):
            if x in words[i]:
                final_list.append(i)
        return final_list
