class Solution(object):
    def canEat(self, candiesCount, queries):
        """
        :type candiesCount: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        s = [0]
        for c in candiesCount:
            s.append(s[-1] + c)

        def answer(t, d, cap):
            max_before = d * cap
            min_before = d
            min_eaten = s[t] - (cap-1)
            max_eaten = s[t+1] - 1
            return max_before >= min_eaten and min_before <= max_eaten
        return [answer(t, d, c) for t, d, c in queries]