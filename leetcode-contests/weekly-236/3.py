import sys

class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        N = len(obstacles)
        
        def bfs():
            q = []
            heapq.heappush(q, (0, 0, 2))
            seen = set()
            while len(q):
                sidejumps, n, lane,  = heapq.heappop(q)
                
                if n == N-1:
                    return sidejumps
                
                #if (n, lane) in seen:
                #    continue
                
                #seen.add((n,lane))
                
                for nincr, sjump in [[1, 0], [0, -1], [0, -2], [0, 1], [0, 2]]:
                    if nincr == 1:
                        #print(n, N)
                        if obstacles[n+1] == lane:
                            continue
                        elif (n+1, lane) not in seen:
                            seen.add((n+1, lane))
                            heapq.heappush(q, (sidejumps, n+1, lane))
                            
                    else:
                        if 1 <= lane + sjump <= 3 and obstacles[n] != (lane + sjump) and (n, lane+sjump) not in seen:
                            seen.add((n, lane+sjump))
                            heapq.heappush(q, (sidejumps + 1, n, lane + sjump))
        
        return bfs()
    