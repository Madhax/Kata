class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        #arr = list(map(abs, arr))
        arr.sort()
        ctr = Counter(arr)
        
        skipZero = False
        #print(arr)
        for x in range(len(arr)):
            val = arr[x]
            #print(val, ctr)
            
            if val == 0:
                if skipZero:
                    skipZero = False
                    continue
                elif ctr[0] >= 2:
                    skipZero = True
                    ctr[0] -= 2
                    continue
                else:
                    return False
            
            elif ctr[val] > 0 and ctr[val*2] > 0:
                ctr[val] -= 1
                ctr[val*2] -= 1
            elif ctr[val] > 0 and val % 2 == 0 and ctr[val//2] > 0:
                ctr[val] -= 1
                ctr[val//2] -= 1
                
            elif ctr[val] == 0:
                continue 
            else:
                return False
                    
        return all(val == 0 for val in ctr.values())
    
        