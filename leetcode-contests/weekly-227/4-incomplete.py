from collections import defaultdict

class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        self.best = defaultdict(lambda: math.inf)
        nums.sort()
        
        d = deque(nums)
        
        newnums = []
        while len(d) > 0:
            x = d.popleft()
            newnums.append(x)
            if len(d) > 0:
                x = d.pop()
                newnums.append(x)
                
        nums = newnums
        
        @lru_cache(maxsize=100000)
        def dp(index, val):
            nonlocal goal, nums

            if index == len(nums):
                return abs(val - goal)
                #return 0
                
            if abs(val - goal) < self.best[index]:
                self.best[index] = abs(val-goal)
                
            elif abs(val-goal) > self.best[index]*(10**2):
                return math.inf
            
            ret = math.inf

            ret = min(ret, dp(index+1, val + nums[index]))
            ret = min(ret, dp(index+1, val))
            
            return ret

        return dp(0, 0)