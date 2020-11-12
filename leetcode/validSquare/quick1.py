class Solution:
    def distance(self,p1,p2):
        x1,y1 = p1
        x2,y2 = p2 
        return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
        
        
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
          
        # if p1==p2 or p1==p3 or p1==p4 or p2==p3 or p2==p4 or p3==p4:
        #     return False

        points = [[p1,p2],[p1,p3],[p1,p4],[p2,p3],[p2,p4],[p3,p4]]
        res=[]

        for i in points:
            res.append(self.distance(i[0],i[1]))
            
        h={}

        for i in res:
            if i not in h:
                h[i] = 1
            else:
                h[i]+=1
        for i in h.values():
            if (i==2 or i==4) and len(h)==2:
                continue
            else:
                return False
        return True