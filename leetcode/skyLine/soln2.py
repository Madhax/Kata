class Solution:
    def getSkyline(self, LRH) -> List[List[int]]:
        skyline = []
        i = 0
        n = len(LRH)
        active = []
        while i<n or active:
            if not active or i<n and LRH[i][0]<=-active[0][1]:
                x=LRH[i][0]
                while i<n and LRH[i][0]<=x:
                    heapq.heappush(active,(-LRH[i][2],-LRH[i][1]) )
                    i+=1 
            else:
                x=-active[0][1]
                while active and -active[0][1]<=x:
                    heapq.heappop(active)
                
            height = 0 if not active else -active[0][0]
            if not skyline or height!=skyline[-1][1]:
                skyline.append([x,height])
        
        return skyline