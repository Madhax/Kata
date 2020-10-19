class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def simple(prices):
            n = len(prices)
            ret = 0
            for x in range(1, n):
                ret += max (0, prices[x] - prices[x-1])
                
            return ret
        
        def dynamic(prices, k):
            n = len(prices)
            dp = [[0 for i in range(n)] for j in range(k+1)]
            
            for x in range(1, k+1):
                prf = -prices[0]
                for j in range(1, n):
                    dp[x][j] = max(dp[x][j-1], prf + prices[j])
                    prf = max(prf, dp[x-1][j-1] - prices[j])
            
            return dp[k][n-1]
        
        if k > len(prices)/2:
            return simple(prices)
        
        return dynamic(prices, k)
    
    
