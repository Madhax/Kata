class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        x = 0
        searchfor = word
        while True:
            if sequence.find(searchfor) >= 0:
                x += 1
                searchfor += word
            else:
                return x