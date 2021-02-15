class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        g = defaultdict(set)
        a = set()
        for i, vs in enumerate(graph):
            for v in vs:
                g[i].add(v)
           
            a.add(i)
           
        b1 = set()
        b2 = set()
       
        b1.add(0)
       
        isAdded = set()
       
        while len(a - isAdded) > 0:
            toAdd = list(a - isAdded)
            willAdd = toAdd[0]
            if len(g[willAdd] & b1) > 0:
                b2.add(willAdd)
            else:
                b1.add(willAdd)
           
            for v in toAdd:
                #print(g[v]&b1)
                """
                if v not in (b1|b2):
                    if len(g[v]&b1) > 0:
                        b2.add(v)

                    if len(g[v]&b2) > 0:
                        b1.add(v)
                """
                if v in b1:
                    for z in g[v]:
                        b2.add(z)

                if v in b2:
                    #print("b2", b2)
                    for z in g[v]:
                        b1.add(z)
           
            isAdded.update(b1)
            isAdded.update(b2)
           
        print(b1, b2)
        return len(b1&b2) == 0