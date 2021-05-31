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


        if i == len(r):
            r += "0"
            

        """
        while int(l) >= int(r):
            #if prev == 124:
            #    print(iter, l, r, l[-1], len(l), len(r))
            if len(l) == len(r)+1:
                #print(iter, l, r, l[-1])
                if l[-1] == "9":
                    #print("here")
                    r += "0"
                elif l[:len(r)] == r:
                    r += str(int(l[-1])+1)
                else: 
                    r += "0"
            elif len(l) > len(r) and l[:len(r)] == r:
                r += l[len(r)]
            else:
                r += "0"
                
            ops += 1

        prev = int(r)
        """
        iter +=  1

    #print(prev)
    return ops
    
if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        _ = input()
        arr = list(map(int, input().split()))
        print(f"Case #{test}: {solve(arr)}")