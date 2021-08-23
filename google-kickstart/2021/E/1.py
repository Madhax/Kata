import sys
from collections import Counter
goal = 0

workStr = ""

sys.setrecursionlimit(10**5)
hist = None
order = []

def buildStr(index, cand):
    if index == goal:
        return True
    #print(order)
    for letter in order:
        if hist[letter] > 0 and workStr[index] != letter:
            hist[letter] -= 1
            cand.append(letter)
            if buildStr(index+1, cand):
                return True
            cand.pop()
            hist[letter] += 1

    return False

def solve(strVal):
    global goal, workStr, hist,order
    workStr = strVal

    goal = len(strVal)

    hist = Counter(strVal)

    maxChars = max(hist.values())
    order = [c for c in hist.keys()]
    order.sort(key = lambda x: hist[x], reverse=True)
    #print(order)
    if maxChars > goal/2:
        #print("HERE")
        return "IMPOSSIBLE"

    cand = []
    if buildStr(0, cand):
        return "".join(cand)

    return "IMPOSSIBLE"

if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        
        strVal = str(input())
        print(f"Case #{test}: {solve(strVal)}")

"""
2
start
jjj
"""