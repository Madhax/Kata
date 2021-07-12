import heapq
from collections import defaultdict

def solve(N, intervals, C):
    events = []

    for key in sorted(intervals.keys()):
        events.append((key, intervals[key]))

    intervalCtr = N
    workHeap = []
    #prev = events[0][0]
    mult = events[0][1]
    #print(events)

    s = [[events[0][0], mult]]

    for x in range(1, len(events)):
        bound, inc = events[x]
        mult += inc
        if inc == -1:
            print(s)
            for x in range(1, len(s)+1):
                print(bound, s[-x][0])
                if bound - s[-x][0] >= 1:
                    print("!", s[-x], bound)
                    heapq.heappush(workHeap, (s[-x][1], bound-s[-x][0]))
                    break

            
            s[-1][0] = bound
            s[-1][1] += inc
            print(bound, inc, s)

        else:
            s.append([bound,mult])

        

    print(workHeap)
    while C > 0 and workHeap:
        mult, coverage = heapq.heappop(workHeap)
        intervalCtr += (mult*max(coverage, C))
        C -= max(coverage, C)

    return intervalCtr

if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        N,C = list(map(int, input().split()))
        events = defaultdict(int)
        for _ in range(1, N+1):
            lb, ub = list(map(int, input().split()))
            #events.append((lb,1))
            #events.append((ub, -1))
            events[lb] += 1
            events[ub] -= 1

        print(f"Case #{test}: {solve(N, events, C)}")

"""
1
3 4 11
10 9
-1 6 7
4 1 6
3 5
2 5 6
9 9 9
9 9
9 9 9

"""