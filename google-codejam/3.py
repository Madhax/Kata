from copy import *

def solve(arr):
    sortedArr = sorted(arr)
    #print(arr, sortedArr)
    cost, i = 0, 0
    
    while i < len(arr)-1:
        j = max(arr.index(sortedArr[i]),i)
        cost += j - i + 1
        arr[:] = arr[:i] + arr[i:j+1][::-1] + arr[j+1:]
        #print(j, i, cost, arr)
        i += 1
    return cost

def build(N, cost):
    if not (N-1 <= cost <= N*(N+1)//2 - 1):
        return "IMPOSSIBLE"
    digits = list(range(1, N+1))
    i = 0
    j = len(digits)-1
    didReverse = False
    while i < j:
        candCost = j - i + 1

        #print(candCost, cost, digits, i, j)
        if candCost + (j-i-1) <= cost:
            #print("here")
            digits[i:j+1] = digits[i:j+1][::-1]
            cost -= candCost 
            if didReverse:
                i += 1
                didReverse=False
            else:
                didReverse=True
                j -= 1
        else:
            #print("here2")
            didReverse = False
            i += 1
            cost -= 1
        #print(digits)
        #i += 1
    if cost == 0:
        return " ".join(map(str, digits))
    else:
        return "IMPOSSIBLE"

if __name__ == "__main__":
    
    #print(build(3,1))
    """
    for N in range(2, 100):
        for C in range(1, 1000):
            try:
                if N-1 <= C <= N*(N+1)//2 - 1:
                    assert C == solve(build(N, C))
                else:
                    assert "IMPOSSIBLE" == build(N, C)
            except:
                #print(x, y)
                print(N, C, build(N, C))
                exit
    print("done")
    """
    t = int(input())
    for test in range(1, t + 1):
        N, C = map(int, input().split())
        #print(digits)
        ret = build(N, C)
        print(f"Case #{test}: {ret}")
    