# https://leetcode.com/problems/check-if-the-sentence-is-pangram/description
# A pangram is a sentence where every letter of the English alphabet appears at least once.
# Given a string sentence containing only lowercase English letters, return true if sentence
# is a pangram, or false otherwise.


# using sets
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = set([chr(i) for i in range(97, 123)])
        sentence = set(sentence)

        if letters == sentence:
            return True

        return False


# iterative approach
class Solution1:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = [chr(i) for i in range(97, 123)]
        
        for char in sentence:
            if char in letters:
                letters.remove(char)

        if letters:
            return False
        
        return True
