import math

def color(A):
    N = len(A)
    M = len(A[0])

    foundSeed = False
    q = []

    for y in range(N):
        for x in range(M):
            if A[y][x] != ".":
                foundSeed = True
                q.append([y,x])
                break

        if foundSeed:
            break

    if len(q) == 0:
        q.append([0,0])
    seen = set()

    while len(q) > 0:
        y, x = q.pop()

        adj = set()

        for c in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            if 0 <= y + c[0] < N and 0 <= x + c[1] < M:
                if (y+c[0], x+c[1]) not in seen:
                    seen.add((y+c[0], x+c[1]))
                    q.append([y+c[0], x+c[1]])

                if A[y+c[0]][x+c[1]] != ".":
                    adj.add(A[y+c[0]][x+c[1]])

        if len(adj) == 2:
            print("NO")
            return

        elif A[y][x] != "." and len(adj) > 0 and A[y][x] == list(adj)[0]:
            print("NO")
            return

        elif A[y][x] == "." and len(adj) == 1:
            color = list(adj)[0]
            if color == "R":
                A[y][x] = "W"
            else:
                A[y][x] = "R"

        elif A[y][x] == "." and len(adj) == 0:
            A[y][x] = "R"

    #output

    print("YES")

    for y in range(N):
        print("".join(A[y]))

    return
    #return numPalindromes % MOD
    
if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        R, C = map(int, input().split())
        A = []

        for _ in range(R):
            row = list(input())
            A.append(row)

        color(A)

"""
1
4 6
......
......
......
......
"""