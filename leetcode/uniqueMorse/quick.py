# Platform: leetcode.com
# No. 804. Unique Morse Code Words
# Link: https://leetcode.com/problems/unique-morse-code-words/
# Difficulty: Easy
# Dev: Chumicat
# Date: 2020/11/15
# Submission: https://leetcode.com/submissions/detail/420221386/
# (Time, Space) Complexity : O(n), O(n)
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        table = {'i': '..', 's': '...', 'd': '-..', 'h': '....', 'l': '.-..', 'b': '-...', 
                 'a': '.-', 'u': '..-', 'k': '-.-', 'v': '...-', 'z': '--..', 'x': '-..-', 
                 'n': '-.', 'r': '.-.', 'g': '--.', 'f': '..-.', 'p': '.--.', 'c': '-.-.', 
                 'm': '--', 'w': '.--', 'o': '---', 'q': '--.-', 'j': '.---', 'y': '-.--', 
                 'e': '.', 't': '-',}
        return len({"".join(table[c] for c in word) for word in words})
