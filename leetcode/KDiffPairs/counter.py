class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ret = 0
        c = collections.Counter(nums)
        
        for key in c:
            if k > 0 and key + k in c:
                ret += 1
            if k == 0 and c[key] > 1:
                ret += 1
        return ret