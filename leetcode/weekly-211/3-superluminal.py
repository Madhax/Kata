class Solution(object):
    def bestTeamScore(self, scores, ages):
        """
        :type scores: List[int]
        :type ages: List[int]
        :rtype: int
        """
        a = [score for _, score in sorted((age, score) for age, score in zip(ages, scores))]
        n = len(a)
        f = a[:]
        for i in xrange(n):
            for j in xrange(i):
                if a[j] <= a[i]:
                    f[i] = max(f[i], a[i] + f[j])
        return max(f)
