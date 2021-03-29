import math

sortedList = []
unSortedList = []
#trinary search
#f = open("test.txt", "a")
def insert(n):

    upper = math.ceil(len(sortedList) * 0.66) 
    lower = math.floor(len(sortedList)* 0.33)

    highlimit = len(sortedList)
    lowlimit = 0

    while lowlimit < highlimit:
        #f.write(f"! {lower} {n} {upper} {sortedList}\n")
        print(f"{sortedList[lower]} {n} {sortedList[upper]}")
        med = int(input())

        if med == sortedList[lower]:
            highlimit = lower
            #f.write(f"upper bound set to {highlimit}, {lowlimit}\n")
            
        elif med == n:
            if lowlimit == lower and highlimit == upper:
                lowlimit += 1
            else:
                lowlimit = lower
                highlimit = upper
            #f.write(f"range bound set to {highlimit}, {lowlimit}\n")
        else:
            lowlimit = upper
            #f.write(f"lower bound set to {highlimit}, {lowlimit}\n")
            if lowlimit == len(sortedList)-1:
                lowlimit+=1
                break

        upper = lowlimit + math.ceil((highlimit-lowlimit) * 0.66) 
        lower = lowlimit + math.floor((highlimit-lowlimit)* 0.33)
        upper = min(len(sortedList)-1, upper)
        #f.write(f"{upper} {lower}\n")
        
    sortedList[:] = sortedList[:lowlimit] + [n] + sortedList[lowlimit:]
    #f.write(f"sortedList {sortedList}\n")
    return

        

    

if __name__ == "__main__":
    T, N, _ = map(int, input().split())
    for test in range(1, T + 1):
        unSortedList = list(range(4, N+1))
        sortedList = []
        print("1 2 3")
        med = int(input())
        if med == 1:
            sortedList.extend([2,1,3])
        elif med == 2:
            sortedList.extend([1,2,3])
        else:
            sortedList.extend([2,3,1])

        for num in unSortedList:
            insert(num)
        
        print(" ".join(map(str, sortedList)))
        if int(input()) == "-1":
            break
        
    