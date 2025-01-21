# https://leetcode.com/problems/reverse-prefix-of-word/description
# Given a 0-indexed string word and a character ch, reverse the segment of word 
# that starts at index 0 and ends at the index of the first occurrence of ch 
# (inclusive). If the character ch does not exist in word, do nothing. Return 
# the resulting string.


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            ch_index = word.index(ch)

            # even if ch is the last string, word[ch_index + 1:] will just return
            # an empty string, so no need for additional index checks
            return word[:ch_index + 1][::-1] + word[ch_index + 1:]
   
        return word
