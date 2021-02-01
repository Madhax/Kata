class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        alt = 0
        maxalt = 0
        for i in gain:
            alt += i
            maxalt = max(alt, maxalt)
        
        return maxalt