class Solution:
    def countPairs(self, n, edges, queries):
        vdeg = {i: 0 for i in range(1, n+1)}
        edeg = defaultdict(int)

        for u, v in map(sorted, edges):
            vdeg[u] += 1
            vdeg[v] += 1
            edeg[u,v] += 1

        nodes = sorted(vdeg, key=vdeg.__getitem__)
        def solve(query):

            #how many |a| + |b| - #(a,b) > query
            #=> how many |a| + |b| > query, minus adjustments

            ans = 0
            j = len(nodes)

            for i, u in enumerate(nodes):
                while j - 1 >= 0 and vdeg[u] + vdeg[nodes[j-1]] > query:
                    j -= 1

                ans += len(nodes) - j
                if vdeg[u] * 2 > query: # subtract (u,u)
                    ans -= 1

            ans >>= 1

            for (u,v), deg in edeg.items():
                if query < vdeg[u] + vdeg[v] <= query + deg:
                    ans -=1

            return ans
        
        return [solve(q) for q in queries]