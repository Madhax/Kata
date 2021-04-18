class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        h = []
        events = [(task[0], task[1], index) for index, task in enumerate(tasks)]
        events.sort(key=lambda x: x[0])
        events = deque(events)
        #print(events)
        
        curTime = 0
        output = []
        while len(h) > 0 or len(events) > 0:
            
        
            while len(events) > 0 and curTime >= events[0][0]:
                (start, worktime, index) = events.popleft()
                heappush(h, (worktime, index, start))
            
            if len(h) > 0:
                (worktime, index, start ) = heappop(h)
                curTime += worktime
                output.append(index)
            elif len(events) > 0:
                curTime = events[0][0]
                    
        return output
