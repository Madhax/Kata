from collections import defaultdict
import math

def solve(nums, k):
    #return max(map(int, list(str(num))))

    output = []
    d = defaultdict(set)
    ctr = [0 for _ in range(k+1)]
    ctr[0] = math.inf

    for val in nums:
        if len(d[val]) >= k:
            output.append(0)
        else:
            curCount, key = min([(x, idx) for idx, x in enumerate(ctr)])
            if key not in d[val]:
                output.append(key)
                d[val].add(key)
            else:
                output.append(0)

    return " ".join(list(map(str, output)))



if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        _, k = list(map(int, input().split()))
        nums = list(map(int, input().split()))
        print(f"{solve(nums, k)}")

"""

1
2
3
4
5
6
7
8
s(9) < s(10)

10 1
11 2
12 3
13 4
14 5
15 6
16 7
17 8
18 9
19 = 10
20 = 2 
"""