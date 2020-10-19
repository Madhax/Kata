class Solution:
    #Version 1: 1D DP
    #TC: O(nk), SC: O(n)
    '''
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def unlimit():
            return sum([max(prices[i] - prices[i-1], 0) for i in range(1, n)])
        
        if not prices or not k:
            return 0
        n = len(prices)
        if k >= n//2:
            return unlimit()
        dp = [0]*n
        for i in range(1, k+1):
            nextDp = [0]*n
            val = dp[0] - prices[0]
            for j in range(n):
                nextDp[j] = max(nextDp[j-1], val + prices[j])
                val = max(val, dp[j] - prices[j])
            dp = nextDp
        return dp[-1]        
    '''
    
    #Version 2: Use variable for every states
    #TC: O(nk), SC: O(k)
    '''
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def unlimit():
            return sum([max(prices[i] - prices[i-1], 0) for i in range(1, n)])
        
        if not prices or not k:
            return 0
        n = len(prices)
        if k >= n//2:
            return unlimit()
        
        buy = [float('inf')]*(k+1)
        sell = [float('-inf')]*(k+1)
        buy[0] = sell[0] = 0
        for num in prices:
            for i in range(1, k+1):
                buy[i] = min(buy[i], num - sell[i-1])
                sell[i] = max(sell[i], num - buy[i])
        return sell[-1]
    '''
    
    #Version 3: Use variable for every states
    #TC: O(nk), SC: O(k)
    '''
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def unlimit():
            return sum([max(prices[i] - prices[i-1], 0) for i in range(1, n)])
        
        if not prices or not k:
            return 0
        n = len(prices)
        if k >= n//2:
            return unlimit()
        
        buy = [float('-inf')]*(k+1)
        sell = [float('-inf')]*(k+1)
        buy[0] = sell[0] = 0
        for num in prices:
            for i in range(1, k+1):
                buy[i] = max(buy[i], sell[i-1] - num)
                sell[i] = max(sell[i], num + buy[i])
        return sell[-1]
    '''
    
    #Version 4: Heap and Stack
    #Let's say we have two pairs of vally and peak. (v1, p1), (v2, p2), v1 < p2 < v2 < p2
    #1. If prices[v2] < prices[v1], for those vallay peak pair which can combine with (v1, p1) can also combine with (v2, p2). Further, it can earn more money by combining with (v2, p2).
    #Therefore, we can pop (v1, p1) pair from the stack.
    #2. If prices[p2] > prices[p1] and prices[v2] >= prices[v1], there is an overlap between these two pairs.
    #If we consider one transaction only, we would have prices[p2] - prices[v1]
    #For two transactions, we would have (prices[p1] - prices[v1]) + (prices[p2] - prices[v2]), in order to get the most beneficial result, we can reorder the profit to be (prices[p2] - prices[v1]) + (prices[p1] - prices[v2]) two transactions.
    #In this way, if we would like to have two transaction here, we can pick both of them, and we can also get the biggest profit for one transaction case.
    #TC: O(n + klogn), SC: O(n)
    #https://leetcode.wang/leetcode-188-Best-Time-to-Buy-and-Sell-StockIV.html
    def maxProfit(self, k: int, prices: List[int]) -> int:
        import heapq
        profit = []
        stack = []
        v = p = 0
        n = len(prices)
        while p < n:
            v = p
            while v+1 < n and prices[v] >= prices[v+1]:
                v += 1
            p = v
            while p+1 < n and prices[p] <= prices[p+1]:
                p += 1
            
            while stack and prices[v] < prices[stack[-1][0]]:
                heapq.heappush(profit, - (prices[stack[-1][1]] - prices[stack[-1][0]]))
                stack.pop()
            
            while stack and prices[p] > prices[stack[-1][1]]:
                heapq.heappush(profit, - (prices[stack[-1][1]] - prices[v]))
                v = stack[-1][0]
                stack.pop()
            if p == v:
                break
            
            stack.append([v, p])
        #print(stack)
        
        while stack:
            src, dst = stack.pop()
            heapq.heappush(profit, -(prices[dst] - prices[src]))
        
        ans = 0
        while k > 0 and profit: 
            ans -= heapq.heappop(profit)
            k -= 1
        return ans
            
                
                
