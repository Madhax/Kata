class Solution:
    def minTimeToType(self, word: str) -> int:
        
        alpha = "abcdefghijklmnopqrstuvwxyz"
        adict = {}
        
        for idx, c in enumerate(alpha):
            adict[c] = idx
            
        
        curPosn = 0
        time = 0
        
        for c in word:
            idx = adict[c]
            minCost = math.inf
            minCost = min(minCost, abs(idx - curPosn))
            minCost = min(minCost, abs((idx+26) - curPosn))
            minCost = min(minCost, abs((idx) - (curPosn+26)))
            time += minCost + 1
            curPosn = idx

        return time