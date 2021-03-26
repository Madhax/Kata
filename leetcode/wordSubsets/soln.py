class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        maxCounter = Counter()
        
        for b in B:
            bCounter = Counter(list(b))
            
            for key in bCounter.keys():
                maxCounter[key] = max(maxCounter[key], bCounter[key])

        #print(maxCounter)
        output = []
    
        for a in A:
            aCounter = Counter(list(a))
            cont = False
            for key in maxCounter.keys():
                if aCounter[key] < maxCounter[key]:
                    cont = True
                    break
            if cont:
                continue
                
            output.append(a)
        
        return output
                