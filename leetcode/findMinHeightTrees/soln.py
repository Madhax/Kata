class Solution:
    connections = {}
    visited = set()
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n < 2:
            return [x for x in range(n)]
                
        self.connections = {}
        self.visited = set()
        for x in range(n):
            self.connections[x] = set()
        
        for edge in edges:
            self.connections[edge[0]].add(edge[1])
            self.connections[edge[1]].add(edge[0])
            
        leaves = []
        for x in range(n):
            if len(self.connections[x]) == 1:
                leaves.append(x)
                
                
        remainder = n
        while remainder > 2:
            remainder -= len(leaves)
            #print(remainder)
            newLeaves = []
            for leaf in leaves:
                for adjacent in self.connections[leaf]:
                    self.connections[adjacent].remove(leaf)
                    if len(self.connections[adjacent]) == 1:
                        newLeaves.append(adjacent)
            leaves = newLeaves
        
        return leaves

        