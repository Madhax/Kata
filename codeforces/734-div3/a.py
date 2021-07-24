import math
def solve(n):
    #return max(map(int, list(str(num))))
    
    digits = int(math.ceil(n/3))

    if 1*digits + 2*digits == n:
        return f"{digits} {digits}"

    elif (digits-1) + (2*digits) == n:
        return f"{digits-1} {(digits)}"

    elif (digits) + (2*(digits-1)) == n:
        return f"{digits} {(digits-1)}"
    


if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        num = int(input())
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