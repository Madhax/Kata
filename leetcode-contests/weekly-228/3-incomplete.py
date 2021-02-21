import heapq
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        h = []
        C = Counter()
        for num in nums:
            #heapq.heappush(h, -num)
            C[num] += 1
            
        print(C)
        print(h)
        
        while maxOperations > 0:
            print(h)
            val = heapq.heappop(h) * -1
            
            if val % 2 == 0:
                val //= 2
                heapq.heappush(h, -val)
            else:
                val1 = floor(val/2)
                val2 = ceil(val/2)
                heapq.heappush(h, -val1)
                heapq.heappush(h, -val2)
                
            maxOperations -= 1
            
        return 0
        #return heapq.heappop(h) * -1