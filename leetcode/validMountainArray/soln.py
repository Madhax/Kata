class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        increasing = True
        hasIncreased = False
        hasDecreased = False
        prev = float("-inf")
        if len(arr) == 1:
            return False
        
        for x in arr:
            if increasing:
                if x < prev and hasIncreased:
                    hasDecreased = True
                    increasing = False
                    prev = x
                    continue
                elif x > prev:
                    if prev != float("-inf"):
                        hasIncreased = True
                    prev = x
                    continue
                else:
                    return False
            else:
                if x >= prev:
                    return False
                
                prev = x
                continue
                
        return True and hasIncreased and hasDecreased