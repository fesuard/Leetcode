# https://leetcode.com/problems/ransom-note/description/
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by
# using the letters from magazine and false otherwise.Each letter in magazine can only be used
# once in ransomNote.


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        res = True
        hashm_ran = {}
        hashm_mag = {}
        for l in ransomNote:
            hashm_ran[l] = hashm_ran.get(l, 0) + 1
        for l in magazine:
            hashm_mag[l] = hashm_mag.get(l, 0) + 1
        for letter in hashm_ran.keys():
            if letter in hashm_mag.keys():
                if hashm_mag[letter] < hashm_ran[letter]:
                    res = False
                    break
            else:
                res = False
                break
        return res
        
