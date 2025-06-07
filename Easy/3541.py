# https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/description
# You are given a string s consisting of lowercase English letters ('a' to 'z').
# Find the vowel with the maximum frequency.
# Find the consonant (all other letters excluding vowels) with the maximum frequency.
# Return the sum of the two frequencies.


# We create a hashmap to store the frequencies of the letters. We iterate through the keys
# and depending if the key/letter is a vowel or not, we store the max vowel frequency and
# the max consonant frequency and we return the sum of those 2.
 class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        hmap = {}
        vowel_freq = 0
        cons_freq = 0

        for letter in s:
            hmap[letter] = hmap.get(letter, 0) + 1

        for key in hmap:
            if key in vowels:
                vowel_freq = max(vowel_freq, hmap[key])
            
            if key not in vowels:
                cons_freq = max(cons_freq, hmap[key])

        return vowel_freq + cons_freq
