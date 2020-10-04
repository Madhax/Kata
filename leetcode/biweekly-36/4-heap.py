
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, K: int, arrival: List[int], load: List[int]) -> List[int]:
        heap = []
        s = SortedList()
        counts = [0] * K
        
        for x in range(K):
            s.add(x)
        
        for i, (a, l) in enumerate(zip(arrival, load)):
            while len(heap) > 0:
                t, index = heap[0]
                if t <= a:
                    heapq.heappop(heap)
                    s.add(index)
                else:
                    break
                    
            k = s.bisect_left(i%K)
            if k >= len(s):
                k = s.bisect_left(0)
                
            if k < len(s):
                counts[s[k]] += 1
                heapq.heappush(heap, (a + l, s[k]))
                #print(i,a, l, s[k])
                s.discard(s[k])
        
        #print(counts)
        results = []
        target = max(counts)
        for x in range(K):
            if counts[x] == target:
                results.append(x)
        return results
