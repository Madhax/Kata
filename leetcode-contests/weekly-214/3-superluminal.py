class Solution(object):
    def maxProfit(self, inventory, orders):
        """
        :type inventory: List[int]
        :type orders: int
        :rtype: int
        """
        arr = inventory
        t = lambda x: x*(x+1)//2
        sell_cnt = lambda x: sum(max(i-x,0) for i in arr)
        sell_amt = lambda x: sum(max(t(i)-t(x),0) for i in arr)
        n = orders
        x, y = 0, max(arr)
        while x + 1 < y:
            z = (x + y) >> 1
            if sell_cnt(z) >= orders: x = z
            else: y = z
        r = sell_amt(y)
        r += y * (orders - sell_cnt(y))
        return r % (10**9 + 7)