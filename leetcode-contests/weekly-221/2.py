from collections import deque
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        
        appleQueue = deque()

        day = 0
        eaten = 0
        lastValidIndex = -1
        
        while day < len(apples) or len(appleQueue) > 0:
            while day < len(days) and len(appleQueue) < days[day]:
                appleQueue.append(0)
            
            if day < len(apples) and days[day] > 0:
                #print(days[day], len(appleQueue))
                appleQueue[days[day]-1] += apples[day]
                
                if days[day]-1 < lastValidIndex:
                    lastValidIndex = days[day]-1
            
            if lastValidIndex < 0 or appleQueue[lastValidIndex] <= 0:
                for iter in range(len(appleQueue)):
                    if appleQueue[iter] > 0:
                        appleQueue[iter] -= 1
                        eaten += 1
                        lastValidIndex = iter
                        break
            else:
                appleQueue[lastValidIndex] -= 1
                eaten += 1
                    
            if len(appleQueue) > 0:
                appleQueue.popleft()
                lastValidIndex -= 1
                
            day += 1
            
        return eaten
            
        
        