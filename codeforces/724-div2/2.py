from collections import deque

def incr(s, index):
    if len(s) == 0:
        s.append('a')
        return

    if s[index] == 'z':
        if index == 0:
            s[index] = 'a'
            s.appendleft('a')
            return
        s[index] = 'a'
        incr(s, index-1)
        return

    s[index] = chr(ord(s[index]) + 1)
    return


def solve(s):
    MEX = deque()

    found = False

    while found == False:
        incr(MEX, len(MEX)-1)
        if "".join(MEX) not in s:
            return "".join(MEX)

    #return numPalindromes % MOD
    
if __name__ == "__main__":

    t = int(input())
    for test in range(1, t + 1):
        _ = input()
        s = input()
        print(f"{solve(s)}")
