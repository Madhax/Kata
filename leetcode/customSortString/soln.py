from collections import Counter
class Solution:
    def customSortString(self, order: str, p: str) -> str:
        
        digCounter = Counter(p)
        output = []
        for val in order:
            if val in digCounter:
                output.extend(val * digCounter[val])
                del digCounter[val]
                
        for key in digCounter.keys():
            output.extend(key * digCounter[key])
            
        #print(output)
        return "".join(output)