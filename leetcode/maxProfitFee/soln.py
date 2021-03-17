class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
       
        @functools.cache
        def dp(i, holding):
           
            if i == len(prices):
                return 0
           
            ret = -math.inf
            if holding:
                #sell
                ret = max(ret, prices[i] - fee + dp(i+1, False))
            else:
                #buy
                ret = max(ret, -prices[i] + dp(i+1, True))
               
            #skip
            ret = max(ret, dp(i+1, holding))
            return ret
       
        return dp(0, False)