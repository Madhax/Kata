import math

def solve(r1, r2):
    
    d1 = {}
    d2 = {}

    base = 2

    for index, val in enumerate(r1):
        d1[val] = index

    for index, val in enumerate(r2):
        d2[val] = index

    worked = set()
    if len(r1) > 2:
        for x in range(1, len(r1)+1):
            if x in worked:
                continue

            posn1 = d1[x]
            val2 = r2[posn1]

            if d1[val2] == d2[x]:
                worked.add(x)
                worked.add(val2)
                base *= 2

    return base % ((10**9) + 7)
    
if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        _ = input()

        r1 = list(map(int, input().split()))
        r2 = list(map(int, input().split()))
        print(f"{solve(r1, r2)}")

"""
1
4
1 2
2 1
"""
