import math

def canWin(myScores, ilyaScores, additionalRounds):

    totalPicks = len(myScores) + additionalRounds
    totalPicks = int(totalPicks - math.floor(totalPicks/4))


    greedily = min(totalPicks, additionalRounds)

    myScore = 100*greedily
    ilyaScore = sum(ilyaScores[:totalPicks])


    totalPicks -= greedily
    #print(totalPicks)
    return myScore + sum(myScores[:totalPicks]) >= ilyaScore

def solve(myScores, ilyaScores):

    totalPicks = len(myScores)
    totalPicks = int(totalPicks - math.floor(totalPicks/4))

    myScores.sort(reverse=True)
    ilyaScores.sort(reverse=True)

    if sum(myScores[:totalPicks]) >= sum(ilyaScores[:totalPicks]):
        return 0

    curRounds = len(myScores)
    #assume greedy

    #binary search

    l = 0
    h = 10000000000
    #print(canWin(myScores, ilyaScores, m))
    
    while l < h:
        m = (l + h) // 2
        if canWin(myScores, ilyaScores, m):
            h = m
        else:
            l = m + 1
    
    return l


if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        _ = input()
        myScores = list(map(int, input().split()))
        ilyaScores = list(map(int, input().split()))
        
        print(f"{solve(myScores, ilyaScores)}")
"""
5
1
100
0
1
0
100
4
20 30 40 50
100 100 100 100
4
10 20 30 40
100 100 100 100
7
7 59 62 52 27 31 55
33 35 50 98 83 80 64


1
4
20 30 40 50
100 100 100 100

"""