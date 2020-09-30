import heapq
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        h = []
        x = 1
        for num in nums:
            if num < x:
                continue
            if num == x:
                x=x+1
                while len(h) and h[0] <= x:
                    if(h[0] == x):
                        x = x + 1
                    heapq.heappop(h)
                    
            if num>x:
                heapq.heappush(h, num)    
            
        return x