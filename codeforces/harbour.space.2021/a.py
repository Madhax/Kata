
def solve(num):
    #return max(map(int, list(str(num))))
    
    base = int(num[:-1] if len(num) > 1 else '0')
    if num[-1] == "9":
        base += 1

    return base
    


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