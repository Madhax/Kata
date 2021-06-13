import math

def solve(s):
    
    candySum = sum(s)

    if candySum % len(s) > 0:
        return -1

    targetAvg = candySum // len(s)

    k = sum([1 for x in s if x > targetAvg])
    return k

    
if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        _ = input()
        A = list(map(int, input().split()))
        print(f"{solve(A)}")

