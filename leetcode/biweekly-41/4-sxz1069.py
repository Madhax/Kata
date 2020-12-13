class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        
        @lru_cache(None)
        def check(idx):
#            print('-----check', idx)
            if idx >= len(boxes): return 0
            startport = boxes[idx][0]
            tripcnt = 0
            flag = True
            sumweight = 0
            tripidx = -1
            for i in range(maxBoxes):
                if idx + i < len(boxes):
                    if startport != boxes[idx+i][0]: 
                        tripcnt += 1
                        tripidx = i
                        startport = boxes[idx+i][0]
                    sumweight += boxes[idx+i][1]
                    if sumweight > maxWeight: break
                else: break
#            print('trip', idx, tripcnt)
            if sumweight > maxWeight: 
                i -= 1
                if boxes[idx+i+1][0] != boxes[idx+i][0]: tripcnt -= 1
#            print('final trip, i, tripidx', idx, tripcnt, i, tripidx)
            if tripcnt == 0: 
                rst = 2 + tripcnt + check(idx + i + 1)
#                print('return 1', idx,":", rst, tripcnt)
                return rst
            else:
                if idx + i + 1 < len(boxes) and boxes[idx+i+1][0] == boxes[idx+i][0]:
#                    print('idx', idx, 'call check', idx+i+1, "and", idx+tripidx)
                    rst = 2 + tripcnt + min(check(idx+i+1), check(idx + tripidx) - 1)
#                    print('return 2', idx,":", rst, tripcnt)
                    return rst
                else: 
                    rst = 2 + tripcnt + check(idx + i + 1)
#                    print('return 3', idx,":", rst, tripcnt)
                    return rst
                        
        return check(0)
            
        