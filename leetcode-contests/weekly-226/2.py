from collections import defaultdict

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        a = defaultdict(list)
        d = defaultdict(int)
        s = set()
        
        for l in adjacentPairs:
            a[l[0]].append(l[1])
            a[l[1]].append(l[0])
            
            s.add(l[1])
            s.add(l[0])
            
            d[l[0]] += 1
            d[l[1]] += 1
            
        #find first one with only 1 adjacent
        
        for key in d.keys():
            if d[key] == 1:
                seed = key
                break
                
        output = [seed]
        
        while len(output) < len(s):
            for adjacent in a[output[-1]]:
                if len(output) == 1:
                    output.append(adjacent)
                
                elif adjacent != output[-2]:
                    output.append(adjacent)
                    break
                #print(adjacent)
            #print(output)
                    
        return output