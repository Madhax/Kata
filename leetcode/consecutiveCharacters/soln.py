class Solution:
    def maxPower(self, s: str) -> int:
        maxLength = 1
        currentChar = ''
        counter = 1
        for c in s:
            if c == currentChar:
                counter += 1
                if counter > maxLength:
                    maxLength = counter
            else:
                counter = 1
                currentChar = c
               
        return maxLength