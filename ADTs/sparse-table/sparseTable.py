import math
def buildSparseTable(arr, n):
    #initialize
    for i in range(n):
        lookup[i][0] = arr[i]

    j = 1
    #compute smaller to larger intervals
    while (1 << j) <= n:
        
        #compute min value for intervals size 2^j
        i = 0
        while (i + (1 << j) - 1) < n:

            if (lookup[i][j-1] < \
                lookup[i + (1 << (j-1))][j-1]):

                lookup[i][j] = lookup[i][j-1]

            else:
                lookup[i][j] = lookup[i + (1<<(j-1))][j-1]

        i += 1
    
    j += 1


def query(L,R):
    j = int(math.log2(R-L+1))

    if lookup[L][j] <= lookup[R-(1<<j)+1][j]:
        return lookup[L][j]

    else:
        return lookup[R-(1<<j)+1][j]

    
3  3  3

3*(9) = 27

6*6 = 36