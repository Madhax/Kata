class Solution:
    def minDeletions(self, s: str) -> int:
        charFrequencies = {}
        distinctFrequencies = {}
        deletions = 0
        for c in s:
            if c in charFrequencies:
                charFrequencies[c] += 1
            else:
                charFrequencies[c] = 1
                
        for c in charFrequencies.keys():
            f = charFrequencies[c]
            if f in distinctFrequencies:
                distinctFrequencies[f] += 1
            else:
                distinctFrequencies[f] = 1
                
        #print(distinctFrequencies)
        
        for df in list(distinctFrequencies.keys()):
            if distinctFrequencies[df] == 1:
                continue
            
            while distinctFrequencies[df] > 1:
                iter = df - 1
                while iter > -1:
                    if iter not in distinctFrequencies:
                        distinctFrequencies[iter] = 1
                        distinctFrequencies[df] -= 1
                        deletions += (df-iter)
                        break
                    if iter == 0:
                        deletions += df
                        distinctFrequencies[df] -= 1
                    iter -= 1
                
            
        return deletions
                