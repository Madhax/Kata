def solve(n,k,x,arr):
    

    arr.sort()

    missed = []
    for c in range(1, len(arr)):
        if arr[c]-arr[c-1] > x:
            missed.append(arr[c]-arr[c-1])

    missed.sort()
    #print(missed)
    iter = 0

    while k > 0 and iter < len(missed):
        if x * 2 >= missed[iter] :
            iter += 1
            k -= 1
        else:
            missed[iter] -= x
            k -= 1

    return len(missed) - iter + 1

if __name__ == "__main__":
    n, k, x = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    print(f"{solve(n,k,x,arr)}")

"""
7 1
abacaba
1 3


8 0 3
1 7
"""