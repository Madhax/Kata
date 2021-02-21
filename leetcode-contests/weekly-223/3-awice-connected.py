class Solution:
    def minimumHammingDistance(self, source, target, edges):
        n = len(source)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen = [False] * n
        ans = 0
        for root in range(n):
            if seen[root]:
                continue

            seen[root] = True
            queue = [root]
            for node in queue:
                for nei in graph[node]:
                    if not seen[nei]:
                        seen[nei] = True
                        queue.append(nei)

            count = defaultdict(int)
            for i in queue:
                count[source[i]] += 1
                count[target[i]] -= 1

            ans += sum(v for v in count.values() if v > 0)
        
        return ans