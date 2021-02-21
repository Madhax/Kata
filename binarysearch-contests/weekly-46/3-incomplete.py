import heapq
class Solution:
    def solve(self, orders):
        
        buyQ = []
        sellQ = []

        for order in orders:
            if order[2] == 0:
                heapq.heappush(buyQ, order)
            else:
                heapq.heappush(sellQ, order)


        
        orders = 0
        pendingOrder = 0
        print(buyQ, sellQ)
        while len(buyQ) > 0 and len(sellQ) > 0:
            (buyval, buyamount, _) = heapq.heappop(buyQ)
            (sellval, sellamount, _) = heapq.heappop(sellQ)
            while len(buyQ) and buyval < sellval:
                (buyval, buyamount, _) = heapq.heappop(buyQ)
              
            print(buyQ, sellQ)

            if buyval < sellval:
                break

            if sellamount >= buyamount:
                orders += (buyamount) 
                pendingOrder = 0
                sellamount -= buyamount
                if sellamount > 0:
                    heapq.heappush(sellQ, [sellval, sellamount, 1])
            else:
                orders += (sellamount)
                buyamount -= sellamount
                heapq.heappush(buyQ, [buyval, buyamount, 0])

        return orders 