def solve(N, M, i, j):
    
    #pick posn1
    if abs(N-i) >= abs(i-N):
        y1 = N
    else:
        y1 = 1

    if abs(M-j) >= abs(j-M):
        x1 = M
    else:
        x1 = 1


    y2 = 1 if y1 > 1 else N
    x2 = 1 if x1 > 1 else M

    print("%d %d %d %d" %(y1,x1,y2,x2))


if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        N,M,i,j = list(map(int, input().split()))
        solve(N,M,i,j)
        #print(f"{}")

