from sortedcontainers import SortedList

class Solution:
    def countPairs(self, N: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        degrees = [0] * N
        elist = collections.defaultdict(lambda: collections.Counter())
        
        for u, v in edges:
            u -= 1
            v -= 1
            
            degrees[u] += 1
            degrees[v] += 1
            
            elist[u][v] += 1
            elist[v][u] += 1
            
        dlist = collections.defaultdict(list)
        for u in range(N):
            #print(u, degrees[u], elist[u])
            for v, c in elist[u].items():
                    #print(u, v, degrees[u], degrees[v], c)
                dlist[u].append((degrees[v], degrees[v] - c))
            #print(u, dlist[u])

        s = SortedList(degrees)
        #print(degrees)
        
        ans = [0] * len(queries)
        
        for u in range(N):
            me = degrees[u]
            s.remove(me)

            for before, after in dlist[u]:
                s.remove(before)
                s.add(after)
                    
            for i, q in enumerate(queries):
                ans[i] += N - s.bisect_right(q - me) - 1
                #print(u, s, me, q, q - me, s.bisect_left(q - me), current)
                
            for before, after in dlist[u]:
                s.remove(after)
                s.add(before)
            s.add(me)

        return list(x // 2 for x in ans)