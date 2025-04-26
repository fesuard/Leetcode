# https://leetcode.com/problems/decode-the-message/description
# You are given the strings key and message, which represent a cipher key and a secret message, respectively. 
# The steps to decode message are as follows:
# Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
# Align the substitution table with the regular English alphabet.
# Each letter in message is then substituted using the table.
# Spaces ' ' are transformed to themselves.


# We use a hashmap to store the characters in 'key' as keys, and the values will be the corresponding letter
# of the alphabet. We then iterate through the characters of 'message' and append to 'res' the value of the
# of the respective character for our hashmap.
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        res = []
        decode_keys = {}
        letter_ord = ord('a')

        for char in key:
            if char != " " and char not in decode_keys:
                decode_keys[char] = chr(letter_ord)
                letter_ord += 1
        
        for char in message:
            if char == " ":
                res.append(" ")
            else:
                res.append(decode_keys[char]) 

        return "".join(res)
      
