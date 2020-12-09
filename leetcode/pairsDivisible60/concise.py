class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        residues = [0] * 60
        res = 0
        for t in time:
            res += residues[-t % 60]
            residues[t % 60] += 1
        
        return res