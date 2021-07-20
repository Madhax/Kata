class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        
        events = defaultdict(int)
        
        for start, end, inc in updates:
            events[start] += inc
            events[end+1] -= inc
            
        incs = []
        
        for key in sorted(events.keys()):
            incs.append((key, events[key]))
            
        #print(incs)
        output = [0 for _ in range(length)]
        
        prev = None
        valAdd = 0
        for start_range, inc in incs:
            
            if prev is not None:
                for x in range(prev, start_range):
                    output[x] = valAdd
            
            prev = start_range
            valAdd += inc
            
        return output
            
        
        
        #updates = list(map(tuple, updates))
        #updates.sort()
        
        
        