import numpy as np

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        adj = np.zeros((n, n))
        for i, node in enumerate(graph):
            for j in node:
                adj[i, j] = 1
        eigs, _ = np.linalg.eigh(adj)
        return (eigs[-1] + eigs[0]) < 1e-10