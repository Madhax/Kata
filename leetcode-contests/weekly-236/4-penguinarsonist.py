from collections import deque

class BIT:
    def __init__(self, n):
        self.n = n
        self.A = [0] * (n+1)
        
    def update(self, I, v):
        while I < self.n:
            self.A[I] += v
            I += I&-I
            
    def query(self, I):
        agg = 0
        while I > 0:
            agg += self.A[I]
            I -= I&-I
        return agg

lim = 10**5
class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.q = deque()
        self.pre = BIT(lim)
        self.counts = BIT(lim)

    def addElement(self, num: int) -> None:
        self.q.append(num)
        self.counts.update(num, 1)
        self.pre.update(num, num)
        
        if len(self.q) > self.m:
            v = self.q.popleft()
            self.counts.update(v, -1)
            self.pre.update(v, -v)

    def calculateMKAverage(self) -> int:
        if len(self.q) < self.m: return -1
        # print(self.q)
        
        lower_sum, upper_sum = None, None
        lo, hi = 0, lim
        while lo <= hi:
            if abs(lo-hi) <= 1:
                lo_v = self.counts.query(lo)
                if lo_v >= self.k:
                    lower_sum = self.pre.query(lo)
                    lower_sum -= lo*(lo_v-self.k)
                else:
                    hi_v = self.counts.query(hi)
                    lower_sum = self.pre.query(hi)
                    lower_sum -= hi*(hi_v-self.k)
                break
            
            mid = (lo+hi)//2
            if self.counts.query(mid) < self.k:
                lo = mid
            else:
                hi = mid    

        lo, hi = 0, lim
        bound = self.m - self.k
        while lo <= hi:
            if abs(lo-hi) <= 1:
                lo_v = self.counts.query(lo)
                if lo_v >= bound:
                    upper_sum = self.pre.query(lo)
                    upper_sum -= lo*(lo_v-bound)
                else:
                    hi_v = self.counts.query(hi)
                    upper_sum = self.pre.query(hi)
                    upper_sum -= hi*(hi_v-bound)
                break
            
            mid = (lo+hi)//2
            if self.counts.query(mid) < bound:
                lo = mid
            else:
                hi = mid    
                
        # print('upper', upper_sum)        
        # print('lower', lower_sum)        
        return (upper_sum - lower_sum) // (self.m - 2*self.k)
    
# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()