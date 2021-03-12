class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
       
        @functools.cache
        def dp(amount):
            #print(amount)
            if amount == 0:
                return 0
           
            ops = math.inf
           
            for coin in coins:
                if coin <= amount:
                    ops = min(ops, 1 + dp(amount-coin))
                else:
                    break
           
            return ops
                   
           
        result = dp(amount)
       
        if result == math.inf:
            return -1
       
        return result
