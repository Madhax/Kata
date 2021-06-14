import math

def solve(A):
    
    work = []
    prev = 0
    if len(A) == 1:
        return A[0]

    for val in A:
        work.append(abs(val-prev))
        prev = val

    work.append(A[-1])

    baseUgly = sum(work)
    ops = 0 
    for x in range(len(A)):
        if x == 0 and x+1 < len(A):
            while A[x] > A[x+1]:
                diff = abs(A[x] - A[x+1])
                work[x] -= diff
                work[x+1] -= diff
                A[x] -= diff
                ops += diff
            
        if 0 <= x - 1 < x + 1 < len(A):
            while A[x-1] < A[x] > A[x+1]:
                diff = min(abs(A[x] - A[x+1]), abs(A[x] - A[x-1]))
                work[x] -= diff
                work[x+1] -= diff
                A[x] -= diff
                ops += diff

        if x == len(A) - 1 and 0 <= x-1:
            while A[x] > A[x-1]:
                diff = abs(A[x] - A[x-1])
                work[x-1] -= diff
                work[x] -= diff
                A[x] -= diff
                ops += diff


    #print(work)
    return sum(work) + ops

    #return numPalindromes % MOD
    
if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        _ = input()

        histogram = list(map(int, input().split()))
        print(f"{solve(histogram)}")

"""
1
4
4 8 9 6

1
1
9
"""
