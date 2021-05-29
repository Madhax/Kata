import sys

t = int(sys.stdin.readline())
for tt in range(1, t + 1):
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline().split()
    arr = [int(x) for x in arr]
    count = 0
    for i in range(1, len(arr)):
        cur = 0
        while arr[i] <= arr[i - 1]:
            arr[i] *= 10
            cur += 1
        print(arr[i], (arr[i] // 10), (10 ** (cur - 1)) - 1)
        if cur > 1 and (arr[i] // 10) + (10 ** (cur - 1)) - 1 > arr[i - 1]:
            cur -= 1
            arr[i] = arr[i - 1] + 1
        print(arr[i])
        count += cur
    print(f"Case #{tt}: {count}")

