class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        n = len(heights)
        
        ans = 0
        
        heap,count,sumI = [],0,0
        
        heapq.heappush(heap,0)
        
        for i in range(1,n):
            
            diff = heights[i] - heights[i-1]
            
            if diff <= 0:
                continue
            
            count += 1
            
            if diff + sumI <= bricks:
                heapq.heappush(heap,-diff)
                sumI += diff
            
            else:
                
                if diff < -heap[0]:
                    sumI += heapq.heappop(heap)
                    heapq.heappush(heap,-diff)
                    sumI += diff
                
                if ladders < count - len(heap) + 1:
                    return i - 1

        
        return n-1
                
            
            
            
                
                