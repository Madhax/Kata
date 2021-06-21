events = []

def solve():
    events.sort(key=lambda x : x[1])

    l = 0
    r = len(events)-1

    moneyNeeded = 0
    productsBought = 0

    while l <= r:
        if productsBought < events[l][1]:
            delta = events[l][1] - productsBought

            cost = min(events[r][0], delta) * 2
            productsBought += min(events[r][0], delta)
            events[r][0] -= min(events[r][0], delta)

            moneyNeeded += cost
            if events[r][0] == 0:
                r -= 1

        else:
            productsBought += events[l][0]
            moneyNeeded += events[l][0]
            l += 1


    return moneyNeeded

if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        required, discount = list(map(int, input().split()))
        events.append([required,discount])
    print(f"{solve()}")
"""
7 1
abacaba
1 3
"""