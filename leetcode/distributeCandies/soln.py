class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
       
        candies = Counter()
        total = 0
        for candy in candyType:
            candies[candy] += 1
            total += 1
           
        return min(total//2, len(candies.keys()))
