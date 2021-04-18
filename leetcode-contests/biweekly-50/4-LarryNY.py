class Solution:
    def makeStringSorted(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        s = list(s)
        N = len(s)

        fact = [1]
        ifact = [pow(1, -1, MOD)]
        for index in range(1, N):
            fact.append((index * fact[-1]) % MOD)
            ifact.append(pow(fact[-1], -1, MOD))

        counts = [0] * 26
        ans = 0
        total = 0
        
        for c in s[::-1]:
            c = ord(c) - ord('a')
            counts[c] += 1
            
            for x in range(c - 1, -1, -1):
                if counts[x] > 0:
                    counts[x] -= 1
                    
                    f = 1
                    for y in counts:
                        if y > 0:
                            f = (f * ifact[y]) % MOD
                    ans += (f * fact[total]) % MOD
                    #print(total, x, fact[total], f, (f * fact[total]) % MOD)
                    ans %= MOD
                    
                    counts[x] += 1
            total += 1
            
        """"
        ans2 = 0
        while s != list(sorted(s)):
            ans2 += 1
            for i in range(N - 1, 0, -1):
                if s[i] < s[i - 1]:
                    break

            for j in range(i, N):
                if s[j] >= s[i - 1]:
                    j -= 1
                    break
                    
            s[i - 1], s[j] = s[j], s[i - 1]
            s[i:] = s[i:][::-1]
            print(ans2, "".join(s))
            
        print(ans, ans2)
        """
        return ans % MOD
