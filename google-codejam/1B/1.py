import itertools

TICKS = 360 * 12 * 10**10

"""

"""

def solve(A,B,C):
    
    for V in itertools.permutations([A,B,C]):
        
        diff = V[1]-V[0]
        
        if diff < 0:
            print(diff)
            diff += TICKS
            print(diff)
            
        for rep in range(12):
            
            #diff == 11*x
            
            tmp = rep * TICKS + diff
            if tmp % 11 == 0:
                
                x = tmp // 11
                shift = V[0] - x

                if shift < 0:
                    shift += TICKS
                
                if (x + shift) % TICKS == V[0] and (12 * x + shift) % TICKS == V[1] and (720 * x + shift) % TICKS == V[2]:
                    print(rep, x, shift)
                    N = x % 1000000000
                    x //= 1000000000
                    
                    S = x % 60
                    x //= 60
                    M = x % 60
                    x //= 60
                    H = x
                    
                    return f"{H} {M} {S} {N}"

if __name__ == "__main__":
     t = int(input())
     for test in range(1, t+1):
         A, B, C = list(map(int, input().split()))
         
         print(f"Case #{test}: {solve(A,B,C)}")