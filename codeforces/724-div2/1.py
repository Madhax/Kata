import math

def solve(s):
    s.sort()

    valSet = set(s)
    if len(s) > len(valSet):
        return "NO"

    newSet = set()

    for x in valSet:
        for y in valSet:
            if x == y:
                continue

            cand = abs(y-x)

            if cand not in valSet or cand not in newSet:
                newSet.add(cand)

            
    valSet |= newSet

    while len(newSet) > 0:
        tmpSet = set()
        for x in valSet:
            for y in newSet:
                if x == y:
                    continue
                
                cand = abs(y-x)

                if cand not in valSet:
                    tmpSet.add(cand)

        valSet |= tmpSet
        newSet = tmpSet
        if len(valSet) > 300:
            return "NO"

    print("YES")
    print(len(valSet))
    return " ".join(map(str, valSet))

    #return numPalindromes % MOD
    
if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        _ = input()
        A = list(map(int, input().split()))
        print(f"{solve(A)}")

"""
1
6 26
bbbaaz

=> aaaaaa
=> baaaab
=> bbaabb
=> bbbbbb
"""