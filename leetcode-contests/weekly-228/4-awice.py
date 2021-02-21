class Solution(object):
    def minTrioDegree(self, n, edges):
        graph = defaultdict(set)
        for u,v  in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        ans = INF = float('inf')
        for u in graph:
            for v, w in edges:
                if v in graph[u] and w in graph[u]:
                    deg = len(graph[u]) + len(graph[v]) + len(graph[w])
                    deg -= 6
                    if deg < ans: ans = deg
        return ans if ans < INF else -1