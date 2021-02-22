class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        return ''.join(c for (a, b) in izip_longest(word1, word2, fillvalue='') for c in (a, b))