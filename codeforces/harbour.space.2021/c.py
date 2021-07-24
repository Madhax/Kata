import math
import functools
mask = ""

"""
0100000000
"""


#maximize team1
@functools.lru_cache(None)
def dp1(index, score1, score2):
    global mask
    if index == 10:
        return index
    
    #endcondition

    if index % 2 == 0:
        #team1 move
        team2moves = (10-index) // 2
        team1moves = (10-index) // 2

        if score1>score2 and abs(score1-score2) > team2moves:
            return index

        if score2>score1 and abs(score1-score2) > team1moves:
            return index

    else:
        team2moves = (10-index+1) // 2
        team1moves = (10-index) // 2

        if score1>score2 and abs(score1-score2) > team2moves:
            return index

        if score2>score1 and abs(score1-score2) > team1moves:
            return index
    
    best = math.inf
    if index % 2 == 0:
        if mask[index] == "?":
            best = min(best, dp1(index+1, score1+1, score2))
        else:
            best = min(best, dp1(index+1, score1+ int(mask[index]), score2))
    else:
        if mask[index] == "?":
            best = min(best, dp1(index+1, score1, score2))

        else:
            best = min(best, dp1(index+1, score1, score2+ int(mask[index])))

    return best

#maximize team2
@functools.lru_cache(None)
def dp2(index, score1, score2):
    global mask
    if index == 10:
        return index
    
    if index % 2 == 0:
        #team1 move
        team2moves = (10-index) // 2
        team1moves = (10-index) // 2

        if score1>score2 and abs(score1-score2) > team2moves:
            return index

        if score2>score1 and abs(score1-score2) > team1moves:
            return index

    else:
        team2moves = (10-index+1) // 2
        team1moves = (10-index) // 2

        if score1>score2 and abs(score1-score2) > team2moves:
            return index

        if score2>score1 and abs(score1-score2) > team1moves:
            return index
    
    best = math.inf
    if index % 2 == 0:
        if mask[index] == "?":
            best = min(best, dp1(index+1, score1, score2))

        else:
            best = min(best, dp1(index+1, score1+ int(mask[index]), score2))
            
    else:
        if mask[index] == "?":
            best = min(best, dp1(index+1, score1, score2+1))

        else:
            best = min(best, dp1(index+1, score1, score2+ int(mask[index])))

    return best

def solve():
    #print(dp1(0, 0, 0), dp2(0, 0, 0))
    return min(dp1(0, 0, 0), dp2(0, 0, 0))

if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        dp1.cache_clear()
        dp2.cache_clear()
        mask = input()
        print(f"{solve()}")

"""
4
1?0???1001
1111111111
??????????
0100000000

"""