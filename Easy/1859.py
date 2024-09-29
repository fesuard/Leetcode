# https://leetcode.com/problems/sorting-the-sentence/description/
# A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word
# consists of lowercase and uppercase English letters. A sentence can be shuffled by appending the 1-indexed word
# position to each word then rearranging the words in the sentence. For example, the sentence "This is a sentence"
# can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3". Given a shuffled sentence s containing
# no more than 9 words, reconstruct and return the original sentence.

class Solution:
    def sortSentence(self, s: str) -> str:
        word_list = s.split()
        sorted_word_list = sorted(word_list, key=lambda x: x[-1])
        final_str = ""
        for w in sorted_word_list:
            final_str += w[:-1] + " "
        return final_str[:-1]
