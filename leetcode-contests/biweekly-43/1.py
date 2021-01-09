class Solution:
    def totalMoney(self, n: int) -> int:
        day = 0
        prevMonday = 0
        prevMoney = 0
        iter = 0
        money = 0
        while iter < n:
            #print(money)
            if day == 0:
                money += (prevMonday+1)
                prevMonday = (prevMonday+1)
                prevMoney = prevMonday
            else:
                money += (prevMoney+1)
                prevMoney+=1
                
            day += 1
            if day == 7:
                day = 0
            iter += 1
        return money
        