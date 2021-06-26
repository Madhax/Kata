
def solve(n):
    arr = []
    if n == 2:
        return "2 1"
    elif n == 3:
        return "3 1 2"

    for x in range(n):
        arr.append(x+1)

    #swap each one
    if n % 2 == 0:
        for x in range(0, n, 2):
            arr[x], arr[x+1] = arr[x+1], arr[x]

    else:
        arr[0], arr[1], arr[2] = arr[2], arr[0], arr[1]
        for x in range(3, n, 2):
            arr[x], arr[x+1] = arr[x+1], arr[x]

    return " ".join(map(str,arr))


if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        n = int(input())
        print(f"{solve(n)}")

"""
4
2
3
4
5


1
4
"""