class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #nums.sort()
       
        @lru_cache(maxsize=None)
        def helper(lval, index, totalLeft):
            nonlocal nums
           
            if index == len(nums):
                return False
           
            if lval > totalLeft:
                return False
           
            if lval == totalLeft:
                return True
           
            if helper(lval + nums[index], index+1, totalLeft-nums[index]):
                return True
           
            elif helper(lval, index+1, totalLeft):
                return True
           
            return False
           
        totalSum = sum(nums)
        if totalSum % 2 != 0: 
            return False
        
        return helper(0, 0, totalSum)