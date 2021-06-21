from collections import Counter

song = ""
preSum = []

def solve(l,r):
    response = 0
    #print(song[l-1:r])
    #c = Counter(song[l-1:r])
    if l - 2 < 0:
        c = preSum[r-1]
    else:
        c = preSum[r-1] - preSum[l-2]

    #print(preSum)
    #for key in c.keys():
    #    response += (ord(key)-ord('a')+1)*c[key]

    return c

if __name__ == "__main__":
    _, t = list(map(int, input().split()))
    song = input()
    ctr = 0
    for val in song:
        ctr += (ord(val)-ord('a')+1)
        preSum.append(ctr)
    for test in range(1, t + 1):
        l, r = list(map(int, input().split()))
        print(f"{solve(l, r)}")
"""
7 1
abacaba
1 3
"""