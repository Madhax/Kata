class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = defaultdict(dict)
        for x, y in edges:
            
            graph[x][y] = True
        
        if graph.get(destination, None) is not None:
            return False
        
        q = deque([(source, {source})])
        seen = {source,}
        while q:
            node, visited = q.popleft()
            if graph.get(node, []) == [] and node != destination:
                return False
            for neighbor in graph.get(node, []):
                if neighbor == destination:
                    continue
                if neighbor not in seen:
                    seen.add(neighbor)
                    visited_ = visited.copy()
                    visited_.add(neighbor)
                    q.append((neighbor, visited_))
                else:
                    if neighbor in visited:
                        return False
                    
        
        return True
        
        
            