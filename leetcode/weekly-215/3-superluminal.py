class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        n = len(nums)
        lhs = {0: 0}
        lhs_cnt = lhs_sum = 0
        rhs_cnt = rhs_sum = 0
        for v in nums:
            lhs_cnt += 1
            lhs_sum += v
            if lhs_sum not in lhs:
                lhs[lhs_sum] = lhs_cnt
        r = lhs.get(x, n + 1)
        for v in reversed(nums):
            rhs_cnt += 1
            rhs_sum += v
            if x - rhs_sum in lhs:
                r = min(r, rhs_cnt + lhs[x - rhs_sum])
        return r if r <= n else -1
