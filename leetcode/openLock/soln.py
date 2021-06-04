class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        seen = {}
        target = tuple(map(int, list(target)))
        
        for deadend in deadends:
            seen[tuple(map(int, list(deadend)))] = True
        
        if (0,0,0,0) in seen:
            return -1
        
        def bfs():
            q = [((0,0,0,0), 0)]
            
            while len(q) > 0:
                comb, cost = q.pop(0)
                
                if comb == target:
                    return cost
                
                for c in range(4):
                    new = list(comb)
                    new[c] = ((comb[c] + 1) % 10)
                    if tuple(new) not in seen:
                        q.append((tuple(new), cost+1))
                        seen[tuple(new)] = True
                        
                    #if comb[c] > 0:
                    new[c] = (comb[c]-1 + 10) % 10
                    if tuple(new) not in seen:
                        q.append((tuple(new), cost+1))
                        seen[tuple(new)] = True
            return -1
        return bfs()