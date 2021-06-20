def solve(s):
    N = len(s)

    curSum = sum(s)
    if curSum/N == 1:
        return 0

    elif curSum/N < 1:
        return 1

    else:
        return curSum - N
    
if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        _ = input()
        A = list(map(int, input().split()))
        print(f"{solve(A)}")

