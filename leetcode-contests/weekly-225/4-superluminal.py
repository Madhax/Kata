class Solution(object):
    def minimumBoxes(self, n):
        """
        :type n: int
        :rtype: int
        """
        pyr = lambda x: (x*(x+1)*(x+2))//6
        tri = lambda x: (x*(x+1))//2
        s = int((6*n)**(1/3.)-2)
        while pyr(s) < n:
            s += 1
        base = tri(s)
        extra = pyr(s)- n
        while extra >= s:
            base -= 1
            extra -= s
            s -= 1
        return base