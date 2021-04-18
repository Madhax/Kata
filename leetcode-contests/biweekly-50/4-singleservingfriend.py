from collections import Counter
MX = 3001
MOD = 10 ** 9 + 7

def power(a, b):
    res = 1
    while b > 0:
        if b % 2 == 1:
            res = res * a % MOD
        a = a * a % MOD
        b //= 2
    return res

def inverse(n):
    return power(n, MOD - 2)

fact = [1]
for i in range(1, MX):
    fact.append(fact[-1] * i % MOD)
fact_inv = [inverse(e) for e in fact]

def calc(s, i, cnt):
    if i == len(s):
        return 0
    res = 0
    for e in range(ord('a'), ord(s[i])):
        ch = chr(e)
        if cnt[ch] > 0:
            cnt[ch] -= 1
            res += total(len(s) - i - 1, cnt)
            res %= MOD
            cnt[ch] += 1
    cnt[s[i]] -= 1
    res += calc(s, i + 1, cnt)
    res %= MOD
    cnt[s[i]] += 1
    return res
    
    
def total(n, cnt):
    res = fact[n]
    for e in cnt.values():
        res *= fact_inv[e]
        res %= MOD
    return res


class Solution:
    def makeStringSorted(self, s: str) -> int:
        cnt = Counter(s)
        return calc(s, 0, cnt)