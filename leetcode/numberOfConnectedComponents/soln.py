class DSU(object):
    def __init__(self, n):
        self.parents = [i for i in range(n)]
    
    def find(self,x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        rootA, rootB = self.find(x), self.find(y)
        if rootA != rootB:
            self.parents[rootA] = rootB
        

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        
        for edge in edges:
            dsu.union(edge[0], edge[1])
            
        coms = set()
        
        for x in range(n):
            coms.add(dsu.find(x))
            
        return len(coms)
        
        
        
        #colour graphs using minimum values, return minimum number of distinct values
        #DSU?
        return 0
        