class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
#         cash = 0
#         balance = -prices[0]
        
#         for i in range(1, len(prices)):
#             cash = max(cash, balance + prices[i] - fee)
#             balance = max(balance, cash - prices[i])
        
#         return cash
        
        
        profit = 0
        curMin = prices[0]
        
        for price in prices:
            if price < curMin:
                curMin = price
            elif price > curMin + fee:
                profit += price - curMin - fee
                curMin = price - fee
        
        return profit

        