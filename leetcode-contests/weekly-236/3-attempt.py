import sys


sys.setrecursionlimit(3000000)

class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        N = len(obstacles)
        """
        def bfs():
            q = []
            heapq.heappush(q, (0, 0, 2))
            seen = set()
            while len(q):
                sidejumps, n, lane,  = heapq.heappop(q)
                
                if n == N-1:
                    return sidejumps
                
                if (n, lane) in seen:
                    continue
                
                seen.add((n,lane))
                
                for nincr, sjump in [[1, 0], [0, -1], [0, -2], [0, 1], [0, 2]]:
                    if nincr == 1:
                        #print(n, N)
                        if obstacles[n+1] == lane:
                            continue
                        elif (n+1, lane) not in seen:
                            heapq.heappush(q, (sidejumps, n+1, lane))
                            
                    else:
                        if 1 <= lane + sjump <= 3 and obstacles[n] != (lane + sjump) and (n, lane+sjump) not in seen:
                            heapq.heappush(q, (sidejumps + 1, n, lane + sjump))
        
        
        def solve():
            #sliding window
            
            curLane = 2
            curPosn = 0
            switches = 0
            while curPosn != N-1:
                
                #iter = 1
                found = False
                lanes = [math.inf, math.inf, math.inf]
                for x in range(curPosn, N):
                    if obstacles[x] > 0:
                        #print(x, obstacles[x])
                        lanes[obstacles[x]-1] = min(lanes[obstacles[x]-1], x)
                        
                    if lanes[0] != math.inf and lanes[1] != math.inf and lanes[2] != math.inf:
                        (posn, lane) = max([(posn, lane+1) for (lane, posn) in enumerate(lanes)])
                        found = True
                        if lane != curLane:
                            curLane = lane
                            switches+=1
                        
                        curPosn = posn-1
                        break
                        if obstacles[curPosn] == curLane:
                            print("HERE")
                        
                #print(curPosn, curLane, lanes, switches)
                if found:
                    continue
                    
                if not all(x != math.inf for x in lanes):
                    if lanes[curLane-1] == math.inf:
                        return switches
                    elif lanes[0] == math.inf and obstacles[curPosn] == 1:
                        return switches+2
                    elif lanes[1] == math.inf and obstacles[curPosn] == 2:
                        return switches+2
                    elif lanes[2] == math.inf and obstacles[curPosn] == 3:
                        return switches+2
                    else:
                        return switches+1
            return switches
                    
        """
        #seen = set()
        @lru_cache(maxsize=10000)
        def dp(n, lane):
            #nonlocal seen
            if n == N-1:
                return 0
            
            best = math.inf
            
            if obstacles[n+1] == lane:
                #need sidejump
                for sjump in [-2, -1, 1, 2]:
                    if 1 <= lane+sjump <= 3 and obstacles[n] != lane+sjump:
                        #seen.add((n, lane+sjump))
                        best = min(best, 1+ dp(n, lane+sjump))
            else:
                best = min(best, dp(n+1, lane))
                    
            return best
        
        return dp(0, 2)