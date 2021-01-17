
class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        maxlen = max(min(a,b) for a,b in rectangles)
        return sum(min(a,b)==maxlen for a,b in rectangles)