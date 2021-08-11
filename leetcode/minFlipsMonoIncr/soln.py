class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
        @functools.cache
        def dp(index, greedy):
            if index == len(s):
                return 0
             
            best = math.inf
            
            if greedy:
                if s[index] == "0":
                    best = min(best, 1 + dp(index+1, True))
                else:
                    best = min(best, dp(index+1, True))
                    
            else:
                #continue non greedy
                if s[index] == "1":
                    best = min(best, 1 + dp(index+1, False))
                else:
                    best = min(best, dp(index+1, False))
                    
                
                #choose greedy
                if s[index] == "1":
                    best = min(best, dp(index+1, True))
                else:
                    best = min(best, 1 + dp(index+1, True))
                
            return best
            
        return min(dp(0, False), dp(0, True))
        