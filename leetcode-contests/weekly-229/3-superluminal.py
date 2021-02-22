class Solution(object):
    def maximumScore(self, nums, multipliers):
        """
        :type nums: List[int]
        :type multipliers: List[int]
        :rtype: int
        """
        """
        at end step, leftmost value will contain result from only choosing right side
        """
        n = len(nums)
        r = [0]
        #DP over each step (i.e. multiple)
        for k, mult in enumerate(multipliers, 1):
            rr = [-float('inf')] * (k+1)
            #i is number of left that has been chosen
            for i in xrange(k+1):
                j = k-i
                #new left is chosen, use previous left value
                if i > 0:
                    rr[i] = max(rr[i], r[i-1] + mult * nums[i-1])
                #right is chosen, use current left value
                if j > 0:
                    rr[i] = max(rr[i], r[i] + mult * nums[n-j])
            #update DP state
            r = rr
        return max(r)