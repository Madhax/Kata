class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        
        isIncreasing = None
        
        peaks = []
        
        for val in target:
            if peaks:
                if val == peaks[-1]:
                    continue
                    
                if isIncreasing:
                    if peaks[-1] < val:
                        peaks.pop()
                    else: 
                        isIncreasing = False
                    peaks.append(val)
                        
                else:
                    if peaks[-1] > val:
                        peaks.pop()
                        
                    else:
                        isIncreasing = True
                    
                    peaks.append(val)
            else:
                peaks.append(val)
                isIncreasing = True
                
            prev = val
            
        if peaks and isIncreasing == False:
            peaks.pop()
            
        print(peaks)
        
        return 0