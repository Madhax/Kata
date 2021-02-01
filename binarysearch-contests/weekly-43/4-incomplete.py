class Solution:
    def solve(self, a, b, k):
        a.sort()
        b.sort()

        for i in range(min(len(a), len(b))):
            if a[i] < 0 and b[i] < 0:
                a[i] = abs(a[i])
                b[i] = abs(b[i])

        a.sort()
        b.sort()
        print(a, b)
        aiter = len(a) - 1
        biter = len(b) - 1
        while k > 0:
            if aiter > 0:
                adiff = a[aiter] - a[aiter-1]
            else:
                adiff = math.inf

            if biter > 0:
                bdiff = b[biter] - b[biter-1]
            else:
                bdiff = math.inf
            
            

            if adiff < bdiff:
                aiter -=1
            else:
                biter -= 1
            #print(adiff, bdiff, aiter, biter)
            k-=1

        return a[aiter] * b[biter]
