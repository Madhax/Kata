class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        n = len(boxes)
        pos = []
        for i, c in enumerate(boxes):
            if c == '1':
                pos.append(i)
        return [sum(abs(j-i) for j in pos) for i in xrange(n)]