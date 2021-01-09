class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        count = 0
        
        while True:
            if word * count not in sequence:
                return count - 1
            count += 1