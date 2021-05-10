import random

class Solution:
    def countPrimes(self, n: int) -> int:
       
        #sieve
        primes = [x for x in range(n+1)]
        #print(primes)
        ctr = 0
        for x in range(2, n):
            if primes[x] > 0:
                ctr += 1
                iter = 2 * x
                while iter < len(primes):
                    primes[iter] = 0
                    iter += x
                #print(primes)
        return ctr
 