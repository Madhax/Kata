class Solution:
    def PrimExample(self):

        def getDist(p1, p2):
            return p1-p2

        g = defaultdict(list)

        for i in range(len(points)):
            for j in range(len(points)):

                graph[i].append((getDist(points[i], points[j]), j))

        start=res=0
        visited = {start}
        pq = []

        for cost, adj in graph[start]:
            heapq.heappush(pq, (cost, adj))

            if next_node not in visited:
                visited.add(next_node)
                res += cost

                for next_cost, adj in graph[next_node]:
                    if adj not in visisted:
                        heapq.heappush(pq, (next_code, adj))

        return res

        
        