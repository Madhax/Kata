import math


MOD = 10**9 + 7
N, K = 0, 0


def solve(s):
    numPalindromes = 0
        
    #if N % 2 == 0:
    mid = N // 2
    if mid == 0:
        return ord(s[0]) - ord('a')
    #ctr = 1
    ctr = 0 
    for x in range(mid):
        mult = min( \
                ((ord(s[x])-ord('a')) + 1),
                ((ord(s[-(x+1)])-ord('a')) + 1), 
                K)
        if ctr == 0:
            ctr = mult
        else:
            ctr *= mult

    if N % 2 == 1:
        centre = (K) * (ctr-1)
        #print("centre", centre)
        if s[:mid] < s[mid+1:]:
            centre += (ord(s[mid]) - ord('a')) + 1
        else:
            centre += (ord(s[mid]) - ord('a'))

        numPalindromes = centre
    else:
        numPalindromes = ctr

    #print(ctr, mid)
    return numPalindromes % MOD
    
if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        N , K = list(map(int, input().split()))
        S = input()
        print(f"Case #{test}: {solve(S)}")

"""
1
6 26
bbbaaz

=> aaaaaa
=> baaaab
=> bbaabb
=> bbbbbb
"""