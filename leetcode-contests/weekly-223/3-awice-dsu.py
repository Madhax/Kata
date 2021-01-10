class Solution:
    def minimumHammingDistance(self, source, target, edges):
        n = len(source)
        dsu = DSU(n)
        for u, v in edges:
            dsu.union(u,v)

        components = defaultdict(int)
        for u in range (n):
            components[dsu.find(u)].append(u)

        ans = 0

        for component in components.values():
            count = defaultdict(int)
            for i in component:
                count[source[i]] += 1
                count[target[i]] -= 1

            ans += sum(v for v in count.values() if v > 0)
        
        return ans