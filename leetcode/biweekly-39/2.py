class Solution:
    def minimumDeletions(self, s: str) -> int:
        """
        Choose posn x, find deletions left, right needed to make it balanced
        minimize posn x
        """
        ad = {}
        bd = {}
        
        bctr = 0
        actr = 0
        for x in range(len(s)):
            bd[x] = bctr
            if s[x]  == "b":
                bctr+=1
                
        for x in range(len(s)-1, -1, -1):
            ad[x] = actr
            if s[x]  == "a":
                actr+=1
                
        bestscore = float("inf")
        bestPosn = 0
        for x in range(len(s)):
            if bd[x] + ad[x] < bestscore:
                bestscore = bd[x] + ad[x]
                bestPosn = x
                
        return bestscore
        #return (bestscore, bestPosn, bd[bestPosn], ad[bestPosn])