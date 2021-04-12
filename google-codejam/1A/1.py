import math

def solve(arr):
    
    prev = -math.inf
    iter = 0
    ops = 0
    while iter < len(arr):
        #print(prev, arr[iter], ops)
        if arr[iter] > prev:
            prev = arr[iter]
            iter += 1
            continue

        l = str(prev)
        r = str(arr[iter])

        if len(l) == len(r):
            r += '0'
            prev = int(r)
            ops += 1
            iter += 1
            continue

        
        i = 0
        while i < len(l) and i < len(r) and l[i] == r[i]:
            i += 1

        #print(l, r)
        if i == len(r):
            if i == len(l):
                r += "0"
                ops += 1

            else:
                app = str(int(l[i:])+1).zfill(len(l)-len(r))
                if len(app) > len(l[i:]):
                    app = "0" * len(app)
                ops += len(app)
                r += app
        
            prev = int(r)
        else:
            while int(l) >= int(r):
                r += "0"
                ops += 1

        prev = int(r)
        iter += 1
        
    #print(prev)
    return ops
    
if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        _ = input()
        arr = list(map(int, input().split()))
        print(f"Case #{test}: {solve(arr)}")