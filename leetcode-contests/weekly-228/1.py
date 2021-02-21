class Solution:
    def minOperations(self, s: str) -> int:
        
        cost1 = 0
        cost2 = 0
        
        for iter in range(len(s)):
            
            #starts at 1
            if iter % 2 == 0:
                if s[iter] == "0":
                    cost1 += 1
                else:
                    cost2 += 1
                
            else:
                if s[iter] == "1":
                    cost1 += 1
                else:
                    cost2 += 1
        
        
        return min(cost1, cost2)