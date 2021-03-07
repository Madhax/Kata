class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        
        weights = defaultdict(lambda : defaultdict(lambda: math.inf))
        paths = defaultdict(set)
        dln = defaultdict(int)
        
        for (u,v,weight) in edges:
            weights[u][v] = weight
            weights[v][u] = weight
            
            paths[u].add(v)
            paths[v].add(u)
            
        seen = set()
        bests = defaultdict(int)
        
        #@functools.cache
        """
        def dp(node):
            if node == n:
                return 0
            
            if node in bests:
                print("here")
                return bests[node]
            
            best = math.inf
            for cand in paths[node]:
                if cand in seen:
                    continue
                    
                seen.add(cand)
                best = min(best, weights[node][cand] +  dp(cand))
                seen.remove(cand)
        
            #bests[node] = best
            return best
            """
        def buildDLN():
            #backwards
            nonlocal dln
            seen = set()
            
            heap = []
            
            heapq.heappush(heap, (0, n))
            #seen.add(n)
            while len(heap) > 0:
                
                (dist, node) = heapq.heappop(heap)
                if node not in seen:
                    seen.add(node)
                    dln[node] = dist
                    for cand in paths[node]:
                        heapq.heappush(heap, (dist+weights[node][cand], cand))
            
        @functools.cache
        def ctr(currentNode):
            nonlocal dln
            #print(currentNode)
            if currentNode == n:
                return 1
            
            ret = 0
            for cand in paths[currentNode]:
                if dln[currentNode] <= dln[cand]:
                    continue
                #print(currentNode, cand)
                ret += ctr(cand)
            
            return ret
                 
            
        """
        for x in range(1, n+1):
            dln[x] = dp(x)
            bests[x] = dln[x]
        """
        buildDLN()
        #print(dln)
        #print(paths)
    
        return ctr(1) % (10**9 + 7)