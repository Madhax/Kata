class Solution:
    def solve(self, points):
        
        xs = defaultdict(list)
        ys = defaultdict(list)

        for (x, y) in points:
            xs[x].append(y)
            ys[y].append(x)

        for val in xs.values():
            val.sort()

        for val in ys.values():
            val.sort()

        
        def getShortest(x, y):
            bestVal = math.inf
            if x in xs:
                i = bisect_left(xs[x], y)
                #print(i, xs[x])
                if i > 0:
                    tmp = abs(y-xs[x][i-1])
                    if tmp > 0:
                        bestVal = min(bestVal, tmp)
                if i < len(xs[x]):
                    tmp = abs(y-xs[x][i])
                    #print("here", tmp, y, xs[x][i])
                    if tmp > 0:
                        bestVal = min(bestVal, tmp)
                    elif i < len(xs[x]) - 1:
                        tmp = abs(y-xs[x][i+1])
                        if tmp > 0:
                            bestVal = min(bestVal, tmp)
            if y in ys:
                i = bisect_left(ys[y], x)
                if i > 0:
                    tmp = abs(x-ys[y][i-1])
                    if tmp > 0:
                        bestVal = min(bestVal, tmp)
                if i < len(ys[y]):
                    tmp = abs(x-ys[y][i])
                    if tmp > 0:
                        bestVal = min(bestVal, tmp)
                    elif i < len(ys[y]) - 1:
                        tmp = abs(x-ys[y][i+1])
                        if tmp > 0:
                            bestVal = min(bestVal, tmp)
            #print(bestVal)
            return bestVal

        output = []
        for (x,y) in points:
            output.append(getShortest(x,y))

        return output