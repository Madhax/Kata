class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        pos = {}
        r = -1
        for i, c in enumerate(s):
            if c in pos:
                r = max(r, i - pos[c] - 1)
            else:
                pos[c] = i
        return r