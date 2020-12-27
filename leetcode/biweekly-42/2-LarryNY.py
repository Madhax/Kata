
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        t = 0
        total = 0
        
        for x, y in customers:
            t = max(x, t)
            
            total += t - x + y
            t += y
        return total / len(customers)