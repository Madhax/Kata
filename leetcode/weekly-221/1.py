class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        l = s[0:len(s)//2]
        r = s[len(s)//2:]
        
        lcount = 0
        rcount = 0
        for vowel in vowels:
            lcount += l.count(vowel)
            rcount += r.count(vowel)
            
        return lcount==rcount
        