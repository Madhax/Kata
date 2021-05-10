import math

def subtractPair(p1, p2):
    """
    4 cases
    1. cover entirely
    2. cover left portion
    3. cover right portion
    4. cover center portion
    5. no coverage
    """
    #case 1
    if p1[0] >= p2[0] and p1[1] <= p2[1]:
        return []

    #case 2
    elif p2[0] <= p1[0] < p2[1]:
        return [[p2[1], p1[1]]]       

    #case 3
    elif p2[0] < p1[1] <= p2[1]:
        return [[p1[0], p2[0]]]

    #case 4
    elif p1[0] < p2[0] and p1[1] > p2[1]:
        return [[p1[0], p2[0]], [p2[1], p1[1]]]

    else:
        return False


def solve(towels):
    rack = []
    ID = 0
    for towel in towels:
        rackiter = 0
        toAdd = []
        while rackiter < len(rack):
            r, towelid = rack[rackiter]
            overlaps = subtractPair(r, towel)
            if overlaps == False:
                rackiter += 1
                continue

            rack.pop(rackiter)

            for overlap in overlaps:
                toAdd.append((overlap, towelid))
        
        rack.append((towel, ID))
        ID += 1
        for add in toAdd:
            rack.append(add)
        

    #print(rack)
    uniqueTowels = set()
    for item in rack:
        uniqueTowels.add(item[1])
        
    return len(uniqueTowels)
    
if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        numTowels = int(input())
        towels = []
        for _ in range(numTowels):
            towel = list(map(int, input().split()))
            towels.append(towel)

        print(f"Case #{test}: {solve(towels)}")