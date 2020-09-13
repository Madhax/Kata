
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        counter = collections.defaultdict(int)
        
        for idx in range(len(secret)):
            s = secret[idx]
            g = guess[idx]
            
            if s == g:
                bulls += 1
            else:
                if counter[s] < 0:
                    cows += 1
                if counter[g] > 0:
                    cows += 1
                counter[s] += 1
                counter[g] -= 1
        return f"{bulls}A{cows}B"