from functools import * 
from bisect import *
class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        
        totalConsumed = []
        total = 0
        for candy in candiesCount:
            total += candy
            totalConsumed.append(total)
            
        #which candy index will I be on if eat dailyCap over X days
        @lru_cache(maxsize=None)
        def getDay(dailyCap, days):
            nonlocal candiesCount, totalConsumed
            
            canConsume = dailyCap * (days+1)
            
            return bisect_left(totalConsumed, canConsume)
            #print("canConsume", canConsume)
        
            index = 0
            #while index < len(candiesCount) and totalConsumed[index] < canConsume:
            #    index += 1
                
            """
            for index in range(len(candiesCount)):
                totalConsumed += candiesCount[index]
                #print(totalConsumed)
                if totalConsumed >= canConsume:
                    #print(totalConsumed, canConsume)
                    return index
            """
            return index
                
            
            """
            index = 0
            candyCount = candiesCount[index]
            daycount = 0
            while daycount < days:
                cap = dailyCap
                
                while cap > 0:
                    rem = min(cap, candyCount)
                    
                    cap -= rem
                    candyCount -= rem
                    
                    if candyCount == 0:
                        #if cap == 0 and days == 1:
                        #    return index
                        
                        index += 1
                        if index == len(candiesCount):
                            return index
                        
                        candyCount = candiesCount[index]
                
                daycount += 1
                
            print(sum(candiesCount[0:days]))
            
            """
            return index
        """
        for (favType, days, cap) in queries:
            print(favType, days, cap)
            print(getDay(cap, days))
            print(getDay(1, days))
        """
        return [getDay(1, days) <= favType <= getDay(cap, days)  for (favType, days, cap) in queries]