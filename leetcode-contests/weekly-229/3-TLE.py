class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        poscache = defaultdict(int)
        negcache = defaultdict(int)
        
        best = -math.inf
        @functools.cache
        def dp(i, j, score):
            nonlocal multipliers, best
            
            step = i + (len(nums) - j - 1)
            #print(step)
            if step== len(multipliers):
                if score > best:
                    best=score
                return
            if i > j:
                return 0
            if score  > 0:
                if step in poscache:
                    if score < poscache[step]:
                        return
                    else:
                        poscache[step] = abs(score)
                else:
                    poscache[step] = abs(score)
            else:
                if step in negcache:
                    if score > negcache[step]:
                        return
                    else:
                        negcache[step] = score
                else:
                    negcache[step] = score
            
            
            #choose i 
            dp(i+1, j, score + nums[i]*multipliers[step])
            dp(i, j-1, score + nums[j]*multipliers[step])
            
            #best = max(best,  + dp(i+1, j))
            #best = max(best, nums[j]*multipliers[step] + dp(i, j-1))

            
        dp(0, len(nums)-1, 0)
        return best