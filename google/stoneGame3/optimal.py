class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        p, pp, ppp = 0, 0, 0
        presum = 0
        
        for i in range(len(stoneValue) - 1, -1, -1):
            presum += stoneValue[i]
            ppp, pp, p = pp, p, presum - min(ppp, pp, p)
        
        a = p
        b = presum - p
        return 'Tie' if a == b else 'Alice' if a > b else 'Bob'