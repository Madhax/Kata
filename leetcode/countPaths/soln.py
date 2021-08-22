class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        goal = n - 1
        g = defaultdict(set)
        
        for u, v, w in roads:
            g[u].add((v,w))
            g[v].add((u,w))
            
        numCount = 0
        minTime = math.inf
        
        def dijkstra():
            nonlocal numCount, minTime
            q = [(0,0)]  
            seen = defaultdict(lambda: math.inf)
            seen[0] = 0
            ways = [0] * (goal+1)
            ways[0] = 1
            while q:
                w, n = heapq.heappop(q)    
                #print(q, minTime, numCount)
                #seen.add(n)
                if seen[n] < w:
                    continue
                    
                for nei, nw in g[n]:
                    if w + nw < seen[nei]:
                        seen[nei] = w + nw
                        ways[nei] = ways[n]
                        heapq.heappush(q, (w+nw, nei))
                        
                    elif w + nw == seen[nei]:
                        ways[nei] += ways[n]        
            
            return ways[goal]
        
    
        return dijkstra() % (10**9 + 7)
 