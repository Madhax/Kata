from functools import lru_cache
class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        
        best = int(binary,2)
        bestVal = binary
        
        @lru_cache(maxsize=None)
        def transform(binary):
            nonlocal best, bestVal

            finding = True
            while finding:
                finding = False
                print(binary)
            
                find = binary.find("10")
                while find != -1:
                    iter = find
                    found = False
                    found = binary.find("0", 0, find) != -1
                    if found:
                        finding = True
                        binary = binary[:find] + "01" + binary[find+2:]
                        break
                        
                    find = binary.find("10", find+1)    
                    
                find = binary.find("00")    
                while find != -1:
                    finding = True
                    binary = binary[:find] + "10" + binary[find+2:]
                    find = binary.find("00", find + 1)
                    
                
            val = int(binary, 2)
            if val > best:
                best = val
                bestVal = binary
        
        transform(binary)
        return bestVal