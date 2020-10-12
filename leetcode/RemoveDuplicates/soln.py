import functools
class Solution:
    allCharacters = set()
    bitMasks = {}
    def removeDuplicateLetters(self, s: str) -> str:
        
        self.allCharacters = set(s)
        mask = 1
        for x in self.allCharacters:
            self.bitMasks[x] = mask
            mask = mask << 1
            
        @lru_cache
        def completeSubsequence(s, index, bitMask):
            if bitMask == 0:
                return True
            
            for x in range(index, len(s)):
                if self.bitMasks[s[x]] & bitMask:
                    return completeSubsequence(s, x+1, bitMask & ~self.bitMasks[s[x]])
                    
            return False
                    
        
        startMask = int("1" * len(self.allCharacters), 2)
        
        
        output = ""
        bestIndex = 0
        while len(output) != len(self.allCharacters):
            bestChar = None
            bestMask = None
            #print(bestIndex)
            for x in range(bestIndex, len(s)):
                if self.bitMasks[s[x]] & startMask and completeSubsequence(s, x+1, startMask & ~self.bitMasks[s[x]]):
                    if bestChar is None:
                        bestChar = s[x]
                        bestMask = self.bitMasks[s[x]]
                        bestIndex = x
                    elif s[x] < bestChar:
                        bestChar = s[x]
                        bestMask = self.bitMasks[s[x]]
                        bestIndex = x
                        
            bestIndex += 1
            output += bestChar
            startMask = startMask & ~bestMask
                    

        
        return output