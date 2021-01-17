from functools import lru_cache
class Solution:
    def solve(self, requests, k):
        userRequests = [x for x in enumerate(requests)]
        #print(userRequests)
        userRequests.sort(key=lambda x: x[1][1])

        print(userRequests)

        #for [i,j] to be k-th there must be at most k other ranges that can fall underneath it

        #@lru_cache(maxsize=None)
        def atMost(j,n):
            nonlocal userRequests
            print(j,n)
            iter = 0
            ctr = 0
            while userRequests[iter][1][0] <= userRequests[j][1][1] and userRequests[j][1][0] <= userRequests[iter][1][1]:
                print(userRequests[iter][1][0], userRequests[j][1][1])
                if j == iter:
                    iter += 1
                    continue

                ctr += 1
                iter += 1
                if ctr == n:
                    return True
            
            return ctr == n

        output = []
        for y in range(len(userRequests)):
            startRequest = userRequests[y]
            if atMost(startRequest[0], k):
                output.append(startRequest[0])
        
        output.sort()
        return output



        