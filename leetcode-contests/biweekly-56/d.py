class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        
        n = len(passingFees)
        
        g = defaultdict(set)
        for u, v, time in edges:
            g[u].add((v, time))
            g[v].add((u,time))
            
            
        
        def bfs():
            
            q = [(passingFees[0], 0, 0)]
            
            seen = defaultdict(lambda: math.inf)
            
            while q:
                
                fees, curNode, curTime = heappop(q)
                #print(fees, curNode, curTime)
                
                if curNode == n-1 and curTime <= maxTime:
                    return fees
                
                
                for nnode, ntime in g[curNode]:
                    
                    if curTime + ntime <= maxTime:
                        if (curNode, nnode) in seen:
                            if seen[(curNode, nnode)] > curTime + ntime:
                                seen[(curNode,nnode)] = curTime + ntime
                                heappush(q, (fees+passingFees[nnode], nnode, curTime+ntime))
                            else:
                                continue
                                
                        else:
                            seen[(curNode,nnode)] = curTime + ntime
                            heappush(q, (fees+passingFees[nnode], nnode, curTime+ntime))
                
            
            return -1
        
        
        return bfs()
        
        
            
        
        
