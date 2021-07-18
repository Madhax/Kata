
def solve(num):
    return max(map(int, list(str(num))))

    


if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        num = int(input())
        print(f"{solve(num)}")

"""
1
4
1 2 3 4
3 1 2 4
2
1 3
2 1
1
0
0
5
4 3 2 1 0
0 1 2 3 4
"""