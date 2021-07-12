from collections import Counter

def solve(orig,jumbled):
    
    ctr1 = Counter()
    ctr2 = Counter()
    for item in orig:
        ctr1 += Counter(item)

    for item in jumbled:
        ctr2 += Counter(item)

    delta = ctr1 - ctr2

    cands = []
    for item in orig:
        if delta == Counter(item):
            cand.append(item)


    if len(cands) == 1:
        return cands[0]

    return ""

    


if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        S, _ = list(map(int, input().split()))
        orig = []
        jumbled = []
        for _ in range(1, S+1):
            orig.append(input())
        for _ in range(1, S):
            jumbled.append(input())
        
        print(f"{solve(orig,jumbled)}")

"""
1
3 5
aaaaa
bbbbb
ccccc
aaaaa
bbbbb
"""