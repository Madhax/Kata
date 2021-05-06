class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        @functools.cache
        def dp(i):
            if i == N - 1:
                return 0
            
            if i >= N:
                return math.inf 
            
            distSize = nums[i]
            jumps = math.inf
            for x in range(distSize, 0, -1):
                #print(x)
                jumps = min(jumps, 1 + dp(i + x))
                
            return jumps
        
        return dp(0)