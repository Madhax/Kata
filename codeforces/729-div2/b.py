from collections import deque
a = 0
b = 0

"""
@functools.lru_cache
def isPossible(n):
    if n == 1:
        return True

    if n < 1:
        return False

    return isPossible(n//a) if n % a == 0 else False or isPossible(n-b)
"""

"""
1+a = 0 (mod a)
1*b = 0 (mod b)




"""
def solve(n):
    if b == 1:
        return "Yes"
    elif b == 2 and n & 1:
        return "Yes"

    elif a == 1 and (n-1) % b == 0:
        return "Yes"

    
    q = deque([1*a, 1+b])

    MODS1 = set()
    MODS2 = set()
    ctr = 0
    while len(q):
        val = q.popleft()

        cand1 = val*a
        cand2 = val+b

        if cand1 == n or cand2 == n:
            return "Yes"
        
        if cand1 < n and n % cand1 not in MODS1:
            q.append(cand1)
            MODS1.add(n%cand1)
        if cand2 < n and n % cand2 not in MODS2:
            q.append(cand2)
            MODS2.add(n%cand2)


    return "No"


if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        n,a,b = list(map(int, input().split()))
        print(f"{solve(n)}")

"""
1
1000000000 2 2

"""