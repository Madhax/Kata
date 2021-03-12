class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def helper(count, have, i, res):
            coin = coins[i]
            if count - (have - amount) // coin >= res:
                return res
            need = amount-have
            if need % coin == 0:
                x = count + need//coin
                return x if x < res else res
            if i == 0:
                return res
            for j in range(need // coin, -1, -1):
                sub = helper(count+j, have+coin*j, i-1, res)
                if sub < res:
                    res = sub
            return res

        coins.sort()
        ret = helper(0, 0, len(coins)-1, amount+1)
        return -1 if ret == amount+1 else ret