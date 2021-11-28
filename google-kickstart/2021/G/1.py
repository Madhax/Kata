import sys
from collections import Counter
goal = 0

workStr = ""

sys.setrecursionlimit(10**5)
hist = None
order = []


def solve(strVal, D, C, M):
    

    for x in range(len(strVal)):
        animal = strVal[x]
        #print(animal, D, C, M)
        if animal == "D" and D == 0:
            return "NO"
        elif animal == "C" and C == 0:
            if "D" in strVal[x:]:
                return "NO"
            else:
                return "YES"
        elif animal == "C":
            C -= 1
        elif animal == "D":
            D -= 1
            C += M

    return "YES"

if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        _, D, C, M = list(map(int, input().split()))
        strVal = str(input())
        print(f"Case #{test}: {solve(strVal, D, C, M)}")

"""
1
4 1 2 0
CCCC
4 2 1 0
DCCD
"""