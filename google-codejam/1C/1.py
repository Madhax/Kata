"""
get winning range from midpoints of tickets bought

check before first, and after last


"""
tickets = []
valuesToCheck = []


def getWinningRange(lval, rval):
    return (max(lval, rval)-min(lval, rval)+1) // 2


"""


4
3 10
1 3 7 7 7 7 7

1
3 10
1 4 5 6 7 

1
4 3
1 2 3 2


1
4 4
1 2 4 2


1
1 4
1 

1
1 4
1 2 3

1
1 30
1 30

29-15

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

1
1 6
1 6


5 4

1 2


1
1 10
1

1
1 30
14 16



1
1 30
1 14 30


1 
1 30
1 1 1 1 1 2 2 2 2 30 30 30 30

1
1 30
1 30



1
1 10
1 10


1
1 11
1 2 11


1
1 10 
1 2 10

2 30


1 
1 29
1 1 11 2 3 11 12 28 29



4
1 30
1 30
1 30
2 29
1 30 
1 29
1 30
2 27

"""

def solve(K, tickets):
    valuesToCheck = []

    possibleToWin = []
    possibleToWinRange = []

    chosen = set(tickets)
    chosenValue = set()
    tickets = list(set(tickets))
    tickets.sort()

    if tickets[0] > 1:
        valuesToCheck.append(tickets[0]-1)
        possibleToWin.append((tickets[0]-1, 1, tickets[0]-1))
        chosenValue.add(tickets[0]-1)
        #print("prepend", ticket[0]-1)

    if tickets[-1] < K:
        valuesToCheck.append(tickets[-1]+1)
        possibleToWin.append(((K+1) - (tickets[-1]+1), tickets[-1]+1, K))
        chosenValue.add(tickets[-1]+1 )
        #print("append", (K+1) - (tickets[-1]+1), K, tickets[-1])
    
    for x in range(1, len(tickets)):
        value = tickets[x]-1
        #print(value)
        if value not in chosenValue and 1 <= value <= K:
            chosenValue.add(value)
            delta = getWinningRange(value, tickets[x-1])
            possibleToWin.append((delta, tickets[x]-delta, tickets[x]-1))
            #print("value", value, tickets[x-1], getWinningRange(value, tickets[x-1]))


        value = tickets[x-1]+1
        #print(value)
        if value not in chosenValue and 1 <= value <= K:
            chosenValue.add(value)
            delta = getWinningRange(value, tickets[x])
            possibleToWin.append((delta, tickets[x-1]+1, tickets[x-1]+delta))
            #print("value", value, tickets[x], getWinningRange(value, tickets[x]))
            #print("here", value)

        
    possibleToWin.sort()
    #print(possibleToWin)
    if len(possibleToWin) == 0:
        return 0
    elif len(possibleToWin) == 1:
        return possibleToWin[-1][0] / K
    else:
        val1 = possibleToWin[-1]
        val2 = possibleToWin[-2]
        if val1[1] == val2[2]:
            probability1 = ((val1[2] - val2[1]) + 1) / K
            if len(possibleToWin) > 2:
                val3 = possibleToWin[-3]
                probability2 = (val1[0] + val3[0]) / K
                return max(probability1, probability2)
            else:
                return probability1
        else:
            return (val1[0] + val2[0]) / K
        #return (possibleToWin[-1] + possibleToWin[-2]) / K
    #return 0




if __name__ == "__main__":
     t = int(input())
     for test in range(1, t+1):
         _, K = list(map(int, input().split()))

         boughtTickets = list(map(int, input().split()))
         boughtTickets.sort()
         print(f"Case #{test}: {solve(K, boughtTickets)}")
