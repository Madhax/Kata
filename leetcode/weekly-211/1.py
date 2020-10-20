class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d = {}
        maxSubstring = -1
        for i, c in enumerate(s):
            if c in d:
                diff = i - d[c] - 1
                if diff > maxSubstring:
                    maxSubstring = diff
                #d[c] = i
            else:
                d[c] = i
        return maxSubstring