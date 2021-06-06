class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = [(e, s) for (e, s) in zip (efficiency, speed)]
        
        engineers.sort(reverse=True)
        q = []
        
        best = 0
        curSum, curMin = 0, math.inf
        curTeam = 0
        #print(engineers)
        for (ee, es) in engineers:
            
            heappush(q, es)
            if len(q) > k:
                s = heappop(q)
                #print(s)
                curSum -= s
            curSum += es
            curTeam = curSum * ee
            if curTeam > best:
                #print(q)
                best = curTeam
            
                
        return best % 1000000007