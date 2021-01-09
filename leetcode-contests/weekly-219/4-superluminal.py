class Solution(object):
    def maxHeight(self, cuboids):
        """
        :type cuboids: List[List[int]]
        :rtype: int
        """
        a = []
        for cube in cuboids:
            a.extend(set(permutations(cube)))
        a.sort(key=lambda (x,y,z):x*y*z)
        f = [z for x,y,z in a]
        for i in xrange(len(a)):
            for j in xrange(i):
                if all(a[j][k]<=a[i][k] for k in xrange(3)):
                    f[i] = max(f[i], f[j] + a[i][2])
        return max(f)