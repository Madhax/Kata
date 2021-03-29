class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        
        buyq = []
        sellq = []
        
        for (price, amount, t) in orders:
            
            #buy
            if t == 0:
                while len(sellq) > 0 and sellq[0][0] <= price and amount > 0:
                    (sellprice, sellamount, t) = heappop(sellq)
                    #print(price, amount)
                    if sellamount >= amount:
                        sellamount -= amount
                        amount = 0
                        
                        heappush(sellq, (sellprice, sellamount, t))
                    else:
                        amount -= sellamount
                        sellamount = 0
                        
                        
                    
                if amount > 0:
                    heappush(buyq, (-price, amount, t))
                    
            elif t == 1:
                while len(buyq) > 0 and (buyq[0][0]*-1) >= price and amount > 0:
                    (buyprice, buyamount, t) = heappop(buyq)
                    buyprice *= -1
                    if buyamount >= amount:
                        buyamount -= amount
                        amount = 0
                        
                        heappush(buyq, (-buyprice, buyamount, t))
                    else:
                        amount -= buyamount
                        buyamount = 0
                        
                
                if amount > 0:
                    heappush(sellq, (price, amount, t))
                
            #print(buyq, sellq)
        
        orders = 0
        for order in buyq:
            orders += order[1]
        
        for order in sellq:
            orders += order[1]
            
        return orders % ((10**9) + 7)