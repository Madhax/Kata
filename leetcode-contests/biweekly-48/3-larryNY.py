class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        N = len(coins)
        
        coins.sort()
        
        mx = 1
        for x in coins:
            if x <= mx:
                mx += x
        return mx