def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if (not(buildings)):
            return([])
        import heapq
        from sys import maxsize
        H = [(0,-maxsize)]
        j=0
        skyline=[]
        while (j<len(buildings)):
            prev_h = -H[0][0]
            x = min(-H[0][1],buildings[j][0])
            while ((-H[0][1]) <= x):
                heapq.heappop(H)
            while ((j<len(buildings)) and (buildings[j][0]==x)):
                B = buildings[j]
                if ((B[2]>-H[0][0]) or (B[1]>-H[0][1])):
                    heapq.heappush(H,(-B[2],-B[1]))
                j+=1
            if (-H[0][0] != prev_h):
                skyline.append([x,-H[0][0]])
        x = (-H[0][1])
        heapq.heappop(H)
        while (-H[0][0]>0):
            if (-H[0][1]>x):
                skyline.append([x,-H[0][0]])
                x = (-H[0][1])
            heapq.heappop(H)
        skyline.append([x,0])        
        return(skyline)