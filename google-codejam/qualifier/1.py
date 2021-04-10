def solve(arr):
    
    sortedArr = sorted(arr)
    #print(arr, sortedArr)
    cost, i = 0, 0
    
    while i < len(arr)-1:
        j = max(arr.index(sortedArr[i]),i)
        cost += j - i + 1
        arr[:] = arr[:i] + arr[i:j+1][::-1] + arr[j+1:]
        #print(j, i, cost, arr)
        i += 1
    return cost

if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        _ = input()
        arr = list(map(int, input().split()))
        print(f"Case #{test}: {solve(arr)}")