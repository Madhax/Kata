class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        g = defaultdict(set)
        
        for u, v in edges:
            g[u].add(v)
            g[v].add(u)
            
        best = 0
        bestConn = 0
        for x in g:
            if len(g[x]) > best:
                bestConn = x
                best = len(g[x])
                
        return bestConn