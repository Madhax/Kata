import itertools
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        goal = Counter(t)
        
        work = deque()
        current = Counter()
        
        bestLen = math.inf
        bestOut = ""
        
        for c in s:
            work.append(c)
            current[c] += 1
            
            while all(current[c] >= goal[c] for c in goal.keys()):
                if len(work) < bestLen:
                    bestOut = "".join(work)
                    bestLen = len(work)
                    
                popped = work.popleft()
                current[popped] -= 1
                if goal[popped] > current[popped]:
                    break
        return bestOut