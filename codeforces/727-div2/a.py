
def solve(n,x,t):
    numDissatisfied = 0

    common = t // x
    if common >= n:
        return (n-1)*(n)//2
    else:
        numDissatisfied =  ((n-common) * common) + ((common-1)*(common)//2)

    #2*2 + (2*3//2) = 4 + 3
    return max(numDissatisfied, 0)
    #2000000000 1 2000000000
if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        n,x,t = list(map(int, input().split()))
        print(f"{solve(n,x,t)}")

"""
4
4 2 5
3 1 2
3 3 10
2000000000 1 2000000000

1999999999000000000
1999999999000000000


1
3 1 3

2
1
0

"""