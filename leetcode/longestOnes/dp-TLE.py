class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        @functools.cache
        def dp(index, k, counting):
            #print(index, k, counting)
            if index == len(nums):
                return 0
            
            best = 0
            
            #continue
            if nums[index] == 1 and counting:
                best = max(best, 1+dp(index+1, k, counting))
            
            #start
            elif nums[index] == 1 and counting == False:
                best = max(best, 1+dp(index+1, k, True))
                best = max(best, dp(index+1, k, counting))
                
                
                
            #continue
            if nums[index] == 0 and counting:
                if k != 0:
                    best = max(best, 1+dp(index+1, k-1, counting))
                    
            
            if nums[index] == 0 and counting == False:
                #start
                if k > 0:
                    best = max(best, 1+dp(index+1, k-1, True))
                    
                #skip - only when not counting
                best = max(best, dp(index+1, k, counting))
                
            """
            if flipsLeft > 0 and nums[index] == 0:
                best = max(best, 1 + dp(index+1, flipsLeft-1, True))
                           
            if nums[index] == 1:
                best = max(best, 1 + dp(index+1, flipsLeft, True))
            
            if nums[index] == 0 and amCounting == False:
                best = max(best, dp(index+1, flipsLeft, False))
            #best = 
            if not (nums[index] == 0 and flipsLeft == 0):
                max(best, dp(index+1, flipsLeft, amCounting))
                
            """
            return best
                
    
        return dp(0, k, False)