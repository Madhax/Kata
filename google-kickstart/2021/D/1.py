import math

def isArithmetic(x,y,z):
    return 1 if x-y == y-z else 0

def solve(arr):
    ctr = 0
    #print("HERE", arr)
    arr[1].append(arr[1][1])

    cands = []
    cands.append((arr[1][0]+arr[1][2])//2)
    cands.append((arr[0][1]+arr[2][1])//2)
    cands.append((arr[0][0]+arr[2][2])//2)
    cands.append((arr[2][0]+arr[0][2])//2)
    best = 0
    #print(cands)
    for cand in cands:
        #row
        ctr = 0
        arr[1][1] = cand
        ctr += isArithmetic(arr[0][0], arr[0][1], arr[0][2])
        ctr += isArithmetic(arr[1][0], arr[1][1], arr[1][2])
        ctr += isArithmetic(arr[2][0], arr[2][1], arr[2][2])

        #column
        ctr += isArithmetic(arr[0][0], arr[1][0], arr[2][0])
        ctr += isArithmetic(arr[0][1], arr[1][1], arr[2][1])
        ctr += isArithmetic(arr[0][2], arr[1][2], arr[2][2])

        #diag
        ctr += isArithmetic(arr[0][0], arr[1][1], arr[2][2])
        ctr += isArithmetic(arr[2][0], arr[1][1], arr[0][2])

        best = max(best, ctr)

    return best

if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        arr = []
        for z in range(3):
            row = list(map(int, input().split()))
            arr.append(row)
        print(f"Case #{test}: {solve(arr)}")

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