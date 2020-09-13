class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bullCount = 0
        cowCount = 0
        secret = list(secret)
        guess = list(guess)
        x = 0
        #get bulls
        while x < len(secret):
            if secret[x] == guess[x]:
                bullCount+=1
                del(secret[x])
                del(guess[x])
            else:
                x+=1
               
               
        for x in guess:
            if x in secret:
                cowCount+=1
                secret.remove(x)
               
        return "%dA%dB" % (bullCount, cowCount)