class Solution:
    def minimumBuckets(self, street: str) -> int:
        minCnt = 0
        
        street = list(street)
        #pass1
        for x in range(1, len(street)-1):
            if street[x-1] == "H" and street[x] == "H" and street[x+1] == "H":
                return -1
    
        for x in range(1, len(street)-1):
            if street[x] == "." and street[x-1] == "H" and street[x+1] == "H":
                street[x-1] = "T"
                street[x] = "T"
                street[x+1] = "T"
                minCnt += 1
        
        for x in range(0, len(street)):
            if street[x] == "." and x > 0 and street[x-1] == "H":
                minCnt += 1
                street[x] = "T"
                street[x-1] = "T"
                
            if street[x] == "." and x+1 < len(street) and street[x+1] == "H":
                minCnt += 1
                street[x] = "T"
                street[x+1] = "T"
       
        return -1 if "H" in street else minCnt
            
            
            
                
