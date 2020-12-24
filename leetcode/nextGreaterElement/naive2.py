from collections import Counter

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        
        seed = [i for i in str(n)]
        best = ['9' for _ in range(len(seed))]
        possibleInts = Counter(seed)
        workingSet = []
        output = float("inf")
        def helper(index, isGreater):
            nonlocal workingSet, seed, possibleInts, n, output, best
            
            if len(workingSet) == len(seed):
                #print(workingSet)
                val = int("".join(workingSet))
                if n < val < output:
                    best = workingSet.copy()
                    output = val
            
            for digit in set(possibleInts.elements()):
                if digit < seed[index] and isGreater==False:
                    continue
                
                if digit > seed[index] and isGreater==False:
                    isGreater=True
                
                if digit > best[index] and isGreater==False:
                    continue
                    
                #print(digit)
                workingSet.append(digit)
                possibleInts[digit] -= 1
                helper(index+1, isGreater)
                possibleInts[digit] += 1
                workingSet.pop()
                
            
        helper(0, False)
        if output == float("inf") or output > 2147483647:
            return -1
        else:
            return output
    
        