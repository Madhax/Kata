from functools import lru_cache
"""
i didnt use line sweep but since everyone is ghosting heres the xiaowuc intuition if it helps

For each request, we break it down into two distinct events - a "start" event and an "end" event, each timestamped by the start and end time of the request respectively.

When a start event is observed, we insert the corresponding request into a set of active request, and when an end event is observed, we remove the corresponding request.

To track which requests could have been the k'th such request, the moment we observe at least k active events, all such active requests could have been the k'th request. We insert those into our answer a set. We keep adding events to our answer set until we have definitively passed the moment where at least k events have expired.
"""
from heapq import *

class Solution:
    def solve(self, requests, k):
        userRequests = [x for x in enumerate(requests)]
        #print(userRequests)
        userRequests.sort(key=lambda x: x[1][0])

        print(userRequests)

        #for [i,j] to be k-th there must be at most k other ranges that can fall underneath it

        h = []
        output = []

        finishedRequests = 0
        active = 0
        for request in userRequests:
            while len(h) > 0 and h[0][1] < request[1][0]:
                req = heappop(h) 
                finishedRequests += 1
                if active >= k:
                    output.append(req[0])
                if finishedRequests >= k:
                    break

            heappush(h, (request[0], request[1][1]))
            active += 1
            print("!", (request[0], request[1][1]))

            #if len(h) >= k+1:
            #    output = [x[0] for x in h]
            #    output.sort()
            #    break
        
        while len(h)> 0:
            req = heappop(h) 
            finishedRequests += 1
            if active >= k:
                output.append(req[0])
            if finishedRequests >= k:
                break
        
        return output



        