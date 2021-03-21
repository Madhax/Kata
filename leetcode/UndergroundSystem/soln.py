class UndergroundSystem:

    def __init__(self):
        self.tally = defaultdict(lambda : defaultdict(lambda : [0,0]))
        self.ids = defaultdict(list)
        
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.ids[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        (startStation, startTime) = self.ids[id]
        self.tally[startStation][stationName][0] += (t-startTime)
        self.tally[startStation][stationName][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        (total, trips) = self.tally[startStation][endStation]
        #print(self.tally)
        return total / trips


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)