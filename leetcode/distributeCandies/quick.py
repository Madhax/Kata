class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        eat = len(candyType)//2
        unique = len(set(candyType))
        
        if unique > eat:
            return eat
        
        else:
            return unique