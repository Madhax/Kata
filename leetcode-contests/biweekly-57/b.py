from sortedcontainers import SortedList
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        events = []
        
        
        for x in range(len(times)):
            events.append((times[x][1], 0, x))
            events.append((times[x][0], 1, x))
            
        events.sort()
        
        availableChairs = SortedList([x for x in range(10**5)])
        friendSeats = {}

        while events:
            _, event, friend = events.pop(0)
            
            if event == 0:
                seat = friendSeats[friend]
                availableChairs.add(seat)
                
            elif event == 1:
                seat = availableChairs[0]
                availableChairs.remove(seat)
                friendSeats[friend] = seat
                
                if friend == targetFriend:
                    return seat
                
        return None
        
            
        #times = [(arrivalTime, endTime, idx) for idx, arrivalTime, endTime in enumerate(times)]
        
        #times.sort()
        
        
