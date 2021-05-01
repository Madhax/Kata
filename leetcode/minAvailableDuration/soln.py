class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])
        
        if slots2[0][0] > slots1[0][0]:
            slots1, slots2 = slots2, slots1
            
            
        #for every end in one check if end + duration does not fall in between a range in slot2
        
        y = 0
        for x in range(len(slots1)):
            
            while y < len(slots2) and slots2[y][1] < slots1[x][0]:
                y += 1
            
            if y == len(slots2):
                break
                
            start = max(slots1[x][0], slots2[y][0])
            end = start + duration
            if slots1[x][0] <= start <= start+duration <= slots1[x][1]:
                if slots2[y][0] <= start <= start+duration <= slots2[y][1]:
                    return [start,end]
            
        
        slots2, slots1 = slots1, slots2
        
        y = 0
        for x in range(len(slots1)):
            
            while y < len(slots2) and slots2[y][1] < slots1[x][0]:
                y += 1
            
            if y == len(slots2):
                break
                
            start = max(slots1[x][0], slots2[y][0])
            end = start + duration
            if slots1[x][0] <= start <= start+duration <= slots1[x][1]:
                if slots2[y][0] <= start <= start+duration <= slots2[y][1]:
                    return [start,end]
    
        return []
            
            
            
            
            
             
            