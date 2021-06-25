class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = defaultdict(set)
        
        for u, v in edges:
            g[u].add(v)
                
        curStack = []
        
        @functools.cache
        def dfs(node):
            #print(node)
            if node == destination:
                return len(g[destination]) == 0
            
            if node in curStack:
                return False
            
            curStack.append(node)
            for nei in g[node]:
                ret = dfs(nei)
                if ret == False:
                    return False
            curStack.pop()
            return len(g[node]) > 0
        
        return dfs(source)
            