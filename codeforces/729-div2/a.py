
def solve(arr):
    odds = 0
    evens = 0

    for val in arr:
        if val & 1:
            odds += 1
        else:
            evens += 1

    
    if odds == evens:
        return "Yes"
    else:
        return "No"


if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        _ = input()
        n = map(int, input().split())
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