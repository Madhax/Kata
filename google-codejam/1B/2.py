U = []
A = 0
B = 0

"""
3
20 1 1 
20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 
20 20 20 
20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 
20 1 20 
20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 
"""
def isGood(start):
    
    testArr = [0] * start
    testArr[start-1] = 1
    #print(testArr, U)
    if len(U) > len(testArr):
        return False

    while True:

        changed = False
        finished = True
        for iter in range(start-1, -1, -1):
            if (iter < len(U) and testArr[iter] > U[iter]) or (iter >= len(U) and testArr[iter] > 0):
                #print(iter, A, B, testArr, U)
                extra = (testArr[iter]-U[iter]) if iter < len(U) else testArr[iter]

                if iter >= A:
                    testArr[iter-A] += extra if iter >= A else 0 
                if iter >= B:
                    testArr[iter-B] += extra if iter >= B else 0
                testArr[iter] -= extra
                changed = True

            if iter < len(U) and iter < len(testArr) and U[iter] > testArr[iter]:
                finished = False

        #print(testArr, finished)
        if finished == True:
            return True
        if changed == False:
            return False

    return 0

def solve():

    maxTries = 500
    iter = 1

    while isGood(iter) == False and iter < maxTries:
        iter += 1

    return iter if iter < maxTries else "IMPOSSIBLE"

if __name__ == "__main__":
    tests = int(input())
    for t in range(1, tests+1):

        _, A, B = map(int, input().split())
        U = list(map(int, input().split()))
        print(f"Case #{t}: {solve()}")

