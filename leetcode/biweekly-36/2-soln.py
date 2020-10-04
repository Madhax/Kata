import collections
class Solution:
    names = []
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def timeToSeconds(time: str):
            time = time.split(":")
            return int(time[1])*60+int(time[0])*3600
        
        self.names = []
        data = {}
        for x in range(0, len(keyName)):
            if keyName[x] in data:
                data[keyName[x]].append(timeToSeconds(keyTime[x]))
            else:
                data[keyName[x]] = [timeToSeconds(keyTime[x])]
                
        for key, value in data.items():
            value.sort()
            deck = collections.deque()
            for time in value:
                
                deck.append(time)
                #print(time, deck[0], time-deck[0], len(deck))
                if time-deck[0] > 3600:
                    deck.popleft()
                if len(deck) >= 3:
                    #print(key)
                    self.names.append(key)
                    break
        
        #print(timeToSeconds("09:55"))
        self.names.sort()
        return self.names
        
        
        