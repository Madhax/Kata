def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    return x % m

MOD = 10 ** 9 + 7

class Fancy(object):

    def __init__(self):
        self.a = []
        self.ops = [[1, 0]]
        

    def append(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.a.append([val, len(self.ops) - 1])
        

    def addAll(self, inc):
        """
        :type inc: int
        :rtype: None
        """
        self.ops.append(self.ops[-1][:])
        self.ops[-1][1] += inc
        self.ops[-1][1] %= MOD
        

    def multAll(self, m):
        """
        :type m: int
        :rtype: None
        """
        self.ops.append(self.ops[-1][:])
        
        self.ops[-1][0] *= m
        self.ops[-1][0] %= MOD
        self.ops[-1][1] *= m
        self.ops[-1][1] %= MOD
        

    def getIndex(self, i):
        """
        :type idx: int
        :rtype: int
        """
        

        if i >= len(self.a): return -1
        v,t = self.a[i]
        a2, b2 = self.ops[-1]
        a1, b1 = self.ops[t]
        
        # want alpha, beta
        alpha = a2 * modinv(a1, MOD) % MOD
        beta = b2 - b1 * alpha
        beta %= MOD
        # print("!", i, a1,b1,';',a2,b2,';',alpha,beta)
        v2 = (alpha * v + beta)%MOD
        return v2
        
        
        


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
