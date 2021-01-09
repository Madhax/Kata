class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        used = [0] * (n+1)
        cands = []
        lastIndex = defaultdict(int)
        
        for x in range(n, 0, -1):
            cands.append(x)
            
        found = True
        best = []
        
        def dfs(sequence):
            nonlocal n, found, used, cands, lastIndex
            #print(len(sequence),   (2 * (n-1)) + 1)          
            if len(sequence) == (2 * (n-1)) + 1:
                best = sequence.copy()
                return sequence
                
            for cand in cands:
                if cand > 1 and used[cand] < 2:
                    if lastIndex[cand] > 0 and (len(sequence)+1 - lastIndex[cand])   == cand:
                        sequence.append(cand)
                        used[cand] += 1
                        if used[cand] == 1:
                            lastIndex[cand] = len(sequence)
                            
                        retVal = dfs(sequence)
                        if retVal is not None:
                            return retVal
                        
                        used[cand] -= 1
                        if used[cand] == 0:
                            lastIndex[cand] = 0
                            
                        sequence.pop()
                        
                    elif lastIndex[cand] == 0 and ((2 * (n-1)) + 1 - len(sequence)  >= cand):
                        sequence.append(cand)
                        used[cand] += 1
                        if used[cand] == 1:
                            lastIndex[cand] = len(sequence)
                            
                        retVal = dfs(sequence)
                        if retVal is not None:
                            return retVal
                        
                        used[cand] -= 1
                        if used[cand] == 0:
                            lastIndex[cand] = 0
                            
                        sequence.pop()
                        
                        
                elif cand == 1 and used[cand] == 0:
                    used[cand] += 1
                    sequence.append(cand)
                    retVal = dfs(sequence)
                    if retVal is not None:
                            return retVal
                        
                    used[cand]-=1
                    sequence.pop()
                    
            return None
                    
                        
        #sequence = []
        return dfs([])