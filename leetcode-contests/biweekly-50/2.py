class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        def dist(x1, y1,x2, y2):
            return sqrt((x2-x1)**2 + (y2-y1)**2)
        
        output = []
        for (x, y, r) in queries:
            cnt = 0
            for x2, y2 in points:
                
                if dist(x,y,x2,y2) <= r:
                    cnt += 1
            output.append(cnt)
            
        return output