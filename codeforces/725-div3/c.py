from collections import defaultdict
from bisect import *

def solve(a, l, r):
    
    #d = Counter(a)

    #memo = defaultdict()
    a = list(set(a))
    a.sort()

    cnt = 0

    for index, val in enumerate(a):
        if val >= l:
            break

        lb = l - val
        if lb <= 0:
            continue

        ub = r - val 

        start = bisect_left(a, lb)
        end = bisect_right(a, ub) 

        print(lb, ub, start, end)
        dist = end - max(start, index+1)
        cnt += dist
        


    return cnt

    
if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        _, l, r = map(int, input().split())
        A = list(map(int, input().split()))
        print(f":{solve(A, l, r)}")

"""
4
3 4 7
5 1 2
5 5 8
5 1 2 4 3
4 100 1000
1 1 1 1
5 9 13
2 5 5 1 1



1
5 5 8
5 1 2 4 3

1
5 9 13
2 5 5 1 1

"""