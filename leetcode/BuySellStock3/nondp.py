class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell1, sell2 = 0, 0
        buy1, buy2 = float('inf'), float('inf')
        
        for p in prices:
            # buy1 = min(buy1, p)
            if p < buy1:
                buy1 = p
            
            # sell1 = max(sell1, p - buy1)
            if p - buy1 > sell1:
                sell1 = p - buy1
            
            # buy2 = min(buy2, p - sell1)
            if p - sell1 < buy2:
                buy2 = p - sell1
                
            # sell2 = max(sell2, p - buy2)
            if p - buy2 > sell2:
                sell2 = p - buy2
                
            
        return sell2