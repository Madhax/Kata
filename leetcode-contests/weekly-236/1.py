class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        val = reduce((lambda x, y: x * y), nums)
        
        if val > 0:
            return 1
        if val < 0:
            return -1
        return 0