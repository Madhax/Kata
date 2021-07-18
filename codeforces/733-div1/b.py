import functools
import sys
sys.setrecursionlimit(50000)
taken = set()
bestPlates = set()
bestNum = 0
curNum = 1
H, W = 0, 0

def isValidChoice(h, w):
    #global taken
    if 0 <= h < H and 0 <= w < W:
        for c in [[-1, -1], [-1, 0], [-1,1], [0, -1], [0,1], [1,-1], [1,0], [1,1], [0,0]]:
            if (h + c[0], w + c[1]) in taken:
                return False

        return True
    
    return False

def getNext(y,x):
    if x == 0:
        if y == H-1:
            return (y, x+1)

        return (y+1, x)

    if y == H-1:
        if x == W-1:
            return (y-1, x)

        return (y, x+1)


    if x == W-1:
        if y == 0:
            return (y, x-1)

        return (y-1, x)

    if y == 0:
        if x == 0:
            return (y+1, x)

        return (y, x-1)

@functools.lru_cache(None)
def recurse(curh, curw):
    global curNum, bestNum, bestPlates
    if curNum > bestNum:
        #print("here", taken)
        bestPlates = taken.copy()
        bestNum = curNum

    
    (ny, nx) = getNext(curh, curw)
    #print(curh, curw, ny,nx)
    if isValidChoice(ny,nx):
        taken.add((ny,nx))
        curNum += 1
        recurse(ny,nx)
        curNum -= 1
        taken.remove((ny,nx))

    (ny, nx) = getNext(ny, nx)

    if isValidChoice(ny,nx):
        taken.add((ny,nx))
        curNum += 1
        recurse(ny,nx)
        curNum -= 1
        taken.remove((ny,nx))

    (ny, nx) = getNext(ny, nx)

    if isValidChoice(ny,nx):
        taken.add((ny,nx))
        curNum += 1
        recurse(ny,nx)
        curNum -= 1
        taken.remove((ny,nx))

    return


def solve():
    global bestPlates
    output = [['0' for _ in range(W)] for _ in range(H)]

    taken.add((0,0))
    recurse(0, 0)
    taken.remove((0,0))
    taken.add((1,0))
    recurse(1, 0)
    taken.remove((1,0))
    taken.add((2,0))
    recurse(2, 0)
    taken.remove((2,0))

    #print(bestPlates)
    for y,x in bestPlates:
        output[y][x] = '1'

    for line in output:
        print("".join(line))

    print("")
    return


if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        H, W = list(map(int, input().split()))
        best = set()
        bestNum = 1
        recurse.cache_clear()
        solve()
        #print(f"{solve(num)}")
"""
1
500 20
4 4
5 6

1
4 4
"""