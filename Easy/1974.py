# https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/description
# There is a special typewriter with lowercase English letters 'a' to 'z' arranged in a 
# circle with a pointer. A character can only be typed if the pointer is pointing to that
# character. The pointer is initially pointing to the character 'a'.


# We start at ascii code 97, since that represents 'a', and for each letter of the given word,
# we add to res the difference between the current ascii code and the ascii code of the letter
# keeping in mind if the difference is greater than 13 or not, since it is a circular typewritter.
# We replace current index with the new letter's index, and add + 1 to res since it takes 1 second
# to type the letter itself.
class Solution:
    def minTimeToType(self, word: str) -> int:
        res = 0
        current_index = 97

        for letter in word:
            difference = abs(ord(letter) - current_index) 
            res += difference if difference < 14 else 26 % difference
            current_index = ord(letter)
            res += 1

        return res
