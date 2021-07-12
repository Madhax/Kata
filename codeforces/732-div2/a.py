
def solve(A,B):
    ops = []

    needToIncrease = []
    needToDecrease = []

    for idx in range(len(A)):
        if A[idx] < B[idx]:
            needToIncrease.append(idx)
        elif A[idx] > B[idx]:
            needToDecrease.append(idx)


    increaseIter = 0
    decreaseIter = 0

    while increaseIter < len(needToIncrease) and decreaseIter < len(needToDecrease):
        ops.append([needToDecrease[decreaseIter]+1, needToIncrease[increaseIter]+1])
        A[needToIncrease[increaseIter]] += 1
        A[needToDecrease[decreaseIter]] -= 1

        if A[needToIncrease[increaseIter]] == B[needToIncrease[increaseIter]]:
            increaseIter += 1

        if A[needToDecrease[decreaseIter]] == B[needToDecrease[decreaseIter]]:
            decreaseIter += 1

    
    canSolve = (increaseIter == len(needToIncrease)) and (decreaseIter == len(needToDecrease))


    if canSolve:
        print(len(ops))
        for op in ops:
            print(" ".join(map(str, op)))

    else:
        print("-1")

    


if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        _ = input()
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        solve(A,B)
        #print(f"{")

"""
1
4
1 2 3 4
3 1 2 4
2
1 3
2 1
1
0
0
5
4 3 2 1 0
0 1 2 3 4
"""