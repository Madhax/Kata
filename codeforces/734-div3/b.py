from collections import Counter

def solve(x):
    #return max(map(int, list(str(num))))
    d = Counter(x)
    
    ret = 0
    ctr = 0

    for key in d.keys():
        if d[key] >= 2:
            ret += 1

        elif d[key] == 1:
            ctr += 1
            if ctr == 2:
                ret += 1
                ctr = 0


    return ret



if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        num = input()
        print(f"{solve(num)}")

"""

1
2
3
4
5
6
7
8
s(9) < s(10)

10 1
11 2
12 3
13 4
14 5
15 6
16 7
17 8
18 9
19 = 10
20 = 2 
"""