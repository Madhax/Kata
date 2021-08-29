class DSU:
    def __init__(self, n):
        self.nodes = [n_ for n_ in range(n)]
        self.ranks = [1 for _ in range(n)]
    
    def find(self, n: int) -> int:
        if self.nodes[n] == n:
            return n
        
        self.nodes[n] = self.find(self.nodes[n])
        
        return self.nodes[n]
    
    def union(self, u: int, v: int) -> bool:
        u_parent = self.find(u)
        v_parent = self.find(v)
        
        if u_parent == v_parent:
            return False
        
        if self.ranks[u_parent] < self.ranks[v_parent]:
            self.nodes[u_parent] = v_parent
        elif self.ranks[u_parent] > self.ranks[v_parent]:
            self.nodes[v_parent] = u_parent
        else:
            self.nodes[v_parent] = u_parent
            self.ranks[u_parent] += self.ranks[v_parent]
        
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        dsu = DSU(n)
        for u, v in edges:
            if not dsu.union(u, v):
                return False
        
        return True