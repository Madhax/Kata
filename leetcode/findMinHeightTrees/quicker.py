class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:        
        graph = {i: [] for i in range(n)}
        
        if n == 1:
            return [0]
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        leaves = []
        for node in graph:
            if len(graph[node]) == 1:
                leaves.append(node)
        
        while n > 2:
            l = len(leaves)
            n -= l
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf][0]
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves
                
                