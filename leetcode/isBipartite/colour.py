class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        def dfs(x, c):
            if x in color: return color[x] == c
            color[x] = c
            return all(dfs(y, -c) for y in graph[x])
        
        return all(i in color or dfs(i, 1) for i in range(len(graph)))