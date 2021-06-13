import math

def solve(s):
    score = 0


    minval = min(s)
    maxval = max(s)

    rev = s[::-1]

    posn1 = s.index(minval)+1
    posn2 = s.index(maxval)+1

    posn3 = rev.index(minval)+1
    posn4 = rev.index(maxval)+1


    return min(max(posn1, posn2), posn1+posn4, posn2+posn3, max(posn3, posn4))

    #return numPalindromes % MOD
    
if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        _ = input()
        A = list(map(int, input().split()))
        print(f"{solve(A)}")

