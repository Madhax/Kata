class Solution(object):
    def minOperations(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        d = sum(nums1) - sum(nums2)
        if d < 0:
            nums1, nums2 = nums2, nums1
            d = -d
        if len(nums1)*1 > len(nums2)*6:
            return -1
        p = [0] * 6
        for x in nums1: p[x-1] += 1
        for x in nums2: p[6-x] += 1
        r = 0
        for i in xrange(5, 0, -1):
            v = min(p[i], (d+i-1)//i)
            d -= i * v
            r += v
            if d < 0: break
        return r
