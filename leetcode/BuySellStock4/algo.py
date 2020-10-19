class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        from heapq import heapify, heappop
        
        if len(prices) < 2:
            return 0
        
        profits = []
        queue = []
        for i in range(1, len(prices)):
            p0, p1 = prices[i-1], prices[i]
            if p1 <= p0:
                continue
                
            while queue:
                q0, q1 = queue[-1]
                if p0 < q0:
                    profits.append(q0 - q1)
                    queue.pop()
                else:
                    break
            
            while queue:
                q0, q1 = queue[-1]
                if q0 <= p0 and q1 < p1:
                    if p0 - q1 < 0:
                        profits.append(p0 - q1)
                    p0, p1 = q0, p1
                    queue.pop()
                else:
                    break
                    
            queue.append((p0, p1))
            
        profits += [p0 - p1 for p0, p1 in queue]
        heapify(profits)
        
        answer = 0
        for _ in range(min(len(profits), k)):
            answer -= heappop(profits)
        return answer
        
    
    # Time: O(nk), Space: O(n+k)
    #
    # dp[i,k] = max(dp[j, k-1] - p[j]) + p[i]  for 0 <= j <= i
    # Keep track of max term as we go to turn quadratic into linear.
    # For each k, keep track of max profit and max diff.
    # 
    # Optimization: for huge k - since max number of trades is bound by n/2,
    # if k exceeds n/2 just make all profitable transactions.
    def maxProfit2(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n / 2 <= k:
            return sum([max(prices[i+1]-prices[i], 0) for i in range(n-1)])
            
        dp = [[0, float('-inf')] for _ in range(k+1)]
        
        for price in prices:
            for j in range(1, k+1):
                profit, maxDiff = dp[j]
                dp[j][0] = max(profit, maxDiff + price)
                dp[j][1] = max(maxDiff, dp[j-1][0] - price)
        
        return dp[-1][0]