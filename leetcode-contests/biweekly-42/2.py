from collections import deque
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        customers.sort(key=lambda x: x[0])
        
        totalWaitTime = 0
        
        startTimes = deque()
        prepTimes = deque()
        
        for customer in customers:
            startTimes.append(customer[0])
            prepTimes.append(customer[1])
            
        
        chefTime = startTimes[0]
        
        while len(startTimes):
            startTime = startTimes.popleft()
            prepTime = prepTimes.popleft()
            
            waitTime = max(chefTime-startTime, 0) + prepTime
            
            totalWaitTime += waitTime
            
            chefTime = max(chefTime+prepTime, startTime+prepTime)
            
            #print(startTime, prepTime, waitTime, chefTime)
            
        return totalWaitTime/len(customers)
    
    