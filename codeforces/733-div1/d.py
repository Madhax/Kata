import math

def solve(prefs):

    result = [0 for _ in range(len(prefs))]
    
    used = set()
    totalPrefs = 0

    for idx, pref in enumerate(prefs):
        if pref in used:
            continue

        result[idx] = pref
        used.add(pref)

    #print(used, result)
    employeeIter = 0

    
    needToAssign = []
    availableNums = []
    for x in range(len(prefs)):
        if result[x] == 0:
            needToAssign.append(x)

    for x in range(1, len(prefs)+1):
        if x not in used:
            availableNums.append(x)

    #special case
    if len(needToAssign) == 1 and needToAssign[-1]+1 == availableNums[-1]:
        for idx, val in enumerate(result):
            if val != 0:
                needToAssign.append(idx)
                availableNums.append(val)
                result[idx] = 0
                break

    needToAssign.sort()
    availableNums.sort()

    if len(needToAssign) > 0:
        needToRotate = False
        for idx, val in zip(needToAssign, availableNums):
            if idx+1 == val:
                needToRotate = True
                break

        while needToRotate:
            availableNums[:] = [availableNums[-1]] + availableNums[0:-1]

            for idx, val in zip(needToAssign, availableNums):
                result[idx] = val

            needToRotate = False
            for idx, val in zip(needToAssign, availableNums):
                if idx+1 == val:
                    needToRotate = True
                    break

    for idx, val in enumerate(result):
        if prefs[idx] == val:
            totalPrefs += 1
            
    """
    for assignment in range(1, len(prefs)+1):
        print(employeeIter, assignment)
        while employeeIter < len(prefs) and result[employeeIter] != 0:
            employeeIter += 1

        if assignment in used:
            continue

        result[employeeIter] = assignment
    """



    print(totalPrefs)
    print(" ".join(list(map(str, result))))

    return 


if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        _ = input()
        prefs = list(map(int, input().split()))
        solve(prefs)
        #print(f"{solve(myScores, ilyaScores)}")
"""
2
3
2 1 2
7
6 4 6 2 4 5 6



1
3
2 1 2
"""