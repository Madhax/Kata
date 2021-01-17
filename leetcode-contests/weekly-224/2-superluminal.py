class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = Counter(a*b for a,b in combinations(nums,2))
        return 4*sum(v*(v-1) for v in c.itervalues())