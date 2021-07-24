import functools
import sys

sys.setrecursionlimit(50000)


start = ""
end = ""

@functools.lru_cache(None)
def recurse(resultIndex, sourceIndex, direction):
    global start, end

    #print(resultIndex, sourceIndex, direction)
    """
    0 = right

    """
    if resultIndex == len(end):
        return True

    if sourceIndex < 0 or sourceIndex >= len(start):
        return False

    if sourceIndex < len(start):
        if start[sourceIndex] != end[resultIndex]:
            return False
    
    ret = False
    #print("HERE")
    #right
    if direction == 0:
        if recurse(resultIndex + 1, sourceIndex + 1, 0):
            return True
        
        if recurse(resultIndex + 1, sourceIndex - 1, 1):
            return True
        """
        if ret:
            return True
        #for x in range(sourceIndex+1, len(start)):
            
            #go left
            if x > 0 and end[resultIndex] == start[x-1]:
                ret = recurse(resultIndex+1, x-1, 1)
            if 
            #keep going right, or pivot left




            if ret:
                return True
            """
    elif direction == 1:
        if recurse(resultIndex+1, sourceIndex-1, 1):
            return True

    return False

def solve():
    global start, end
    x = -1
    if len(end) == 1:
        if start.find(end) > 0:
            return "YES"

    while (x := start.find(end[0], x+1)) > -1:
        #print(x)
        if recurse(1, x+1, 0) or recurse(1, x-1, 1):
            return "YES"

    return "NO"

if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        recurse.cache_clear()
        start = input()
        end = input()
        print(f"{solve()}")

"""
6
abcdef
cdedcb
aaa
aaaaa
aab
baaa
ab
b
abcdef
abcdef
ba
baa


1
aab
baaa
"""