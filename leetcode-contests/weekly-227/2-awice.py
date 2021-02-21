class Solution(object):
    def maximumScore(self, a, b, c):
        a,b,c = sorted([a,b,c])
        c = min(c, a + b)
        return (a+b+c)//2