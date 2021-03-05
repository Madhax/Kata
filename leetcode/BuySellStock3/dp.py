class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        @functools.cache
        def dp(numSold, dayIter, holding):
           
            if numSold == 2:
                return 0
           
            if dayIter == len(prices):
                return 0

            #if not hold, buy
            if holding:
                return max(dp(numSold, dayIter + 1, True), prices[dayIter] +  dp(numSold+1, dayIter + 1, False))
               
            else:
                return max(-prices[dayIter] + dp(numSold, dayIter + 1, True), dp(numSold, dayIter+1, False))
           
            return ret
       
       
        return dp(0, 0, False)