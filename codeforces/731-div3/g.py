from collections import defaultdict
from collections import deque
import functools
import math

g = defaultdict(set)
seen = set()

@functools.lru_cache(None)
def dfs(node, dest):
    #print(node)
    if node == dest:
        ret = 1
    else:
        ret = 0

    
    #ret = 0

    for nnode in g[node]:
        if nnode not in seen:
            seen.add(node)
            ret += dfs(nnode, dest)
            seen.remove(node)    
        else:
            ret += math.inf if dest in seen else 0
            break

    
    return ret

def solve(N):
    output = []
    print(N, g)
    print(dfs(1,3))
    """
    for x in range(1, N+1):
        val = dfs(1, x)
        if val == math.inf:
            output.append(-1)
        else:
            output.append(min(val, 2))
    """
    return " ".join(map(str, output))


if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        g = defaultdict(set)
        N, E = map(int, input().split())
        for _ in range(1, E+1):
            u,v = map(int, input().split())
            g[u].add(v)
        
        print(f"{solve(N)}")


"""
1
6 7
1 4
1 3
3 4
4 5
2 1
5 5
5 6

"""