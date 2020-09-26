class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_dict, guess_dict = defaultdict(int), defaultdict(int)
        bull = cow = 0
        
        for s, g in zip(secret, guess):
            if s == g:
                bull += 1
            else:
                guess_dict[g] += 1
                secret_dict[s] += 1
        
        for guess in guess_dict:
            if guess in secret_dict:
                cow += min(guess_dict[guess], secret_dict[guess])
            
        return f"{bull}A{cow}B"
       
