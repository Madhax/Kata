class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s = set()
        
        curint = []
        
        for c in word:
            if '0' <= c <= '9':
                curint += c
            else:
                if len(curint) > 0:
                    s.add(int("".join(curint)))
                    curint = []
        if len(curint) > 0:
            s.add(int("".join(curint)))
            curint = []
        #print(s)
        return len(s)