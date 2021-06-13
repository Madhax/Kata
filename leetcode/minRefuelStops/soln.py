class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
            
        stations.sort(key=lambda x: x[0])
        
        q = []
        
        currentDistance = startFuel
        refuels = 0
        
        while True:
            #print(stations, q, currentDistance)
            if currentDistance >= target:
                break
                
            if len(stations) == 0 and len(q) == 0:
                return -1
            
            while len(stations) and currentDistance >= stations[0][0]:
                _, fuel = stations.pop(0)
                
                heappush(q, -fuel)
                
                
            if len(q) == 0:
                return -1
            
            fuel = heappop(q)
            currentDistance += -fuel
            refuels += 1
        
        return refuels