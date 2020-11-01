class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        # n balls into 5 urns = n+4 choose 4
        return ((n+4)*(n+3)*(n+2)*(n+1))//24