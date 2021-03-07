class Solution(object):
    def getCollisionTimes(self, cars):
        """
        :type cars: List[List[int]]
        :rtype: List[float]
        """
        n = len(cars)
        r = [-1] * n
        stack = []
        for i in xrange(n-1, -1, -1):
            pos, speed = cars[i]
            while stack and cars[i][1] <= stack[-1][1]:
                stack.pop()
            while len(stack) >= 2:
                t1 = (stack[-1][0]-cars[i][0]) * (stack[-1][1]-stack[-2][1])
                t2 = (stack[-2][0]-stack[-1][0]) * (cars[i][1]-stack[-1][1])
                if t1 < t2: break
                stack.pop()
            if stack:
                r[i] = float(stack[-1][0]-cars[i][0]) / float(cars[i][1]-stack[-1][1])
            stack.append(cars[i])
        return r