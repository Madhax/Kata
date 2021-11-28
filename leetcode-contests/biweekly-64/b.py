class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        curBest = 0
        #maximize values to the left
        events.sort()
        eventsr = events[::-1]
        
        #sort by end
        events.sort(key=lambda x: x[1])
        
        lmax = {}
        rmax = {}
        
        curMax = -math.inf
        for cand in events:
            curBest = max(curBest, cand[2])
            curMax = max(cand[2], curMax)
            lmax[cand[1]] = curMax
            
        curMax = -math.inf
        for cand in eventsr:
            curMax = max(cand[2], curMax)
            rmax[cand[0]] = curMax
            
            
        lkeys = sorted(list(lmax.keys()))
        rkeys = sorted(list(rmax.keys()))
        
        l = 0
        r = 0
        
        
        
        curlkey = lkeys[0]
        currkey = rkeys[0]
        
        #print(lmax)
        #print(rmax)
        #print(lkeys)
        #print(rkeys)
        while l < len(lkeys):
            curlkey = lkeys[l]
            while r < len(rkeys) and currkey <= curlkey:
                r += 1
                if r == len(rkeys):
                    break
                currkey = rkeys[r]
                
            if r == len(rkeys):
                break     
                
            curBest = max(curBest, lmax[curlkey] + rmax[currkey])
            
            l += 1
            
        
        #print(lmax)
        #print(rmax)
        
        return curBest
        
