class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        if word1 == word2:
            return True
        
        w1 = list(word1)
        w2 = list(word2)
        
        w1.sort()
        w2.sort()
        
        s1 = set(w1)
        s2 = set(w2)
        
        if s1 != s2:
            return False
        
        ls1 = []
        ls2 = []
        
        for char in s1:
            ls1.append(w1.count(char))
            
        for char in s2:
            ls2.append(w2.count(char))
            
        ls1.sort()
        ls2.sort()
        
        if ls1 != ls2:
            return False
        
        return True
    
        """
        def dScore(w1, w2):
            score = 0
            for c1, c2 in zip(w1,w2):
                if c1 != c2:
                    score += 1
            
            return score
        
        
        def processWord(w1, w2, score):
            #print(w1, w2, score)
            #swap existing characters
            chars = list(set(w1))
            #print(chars)
            for x in range(len(chars)):
                for y in range(x+1, len(chars)):
                    #print(x)
                    c1 = chars[x]
                    c2 = chars[y]
                    #print(c1, c2)
                    wcopy = w1.copy()
                    for z in range(len(wcopy)):
                        if wcopy[z] == c1:
                            wcopy[z] = c2
                        elif wcopy[z] == c2:
                            wcopy[z] = c1
                            
                    
                    wcopy.sort()
                    #print("wcopy", wcopy)
                    newscore = dScore(wcopy, w2)
                    #print(newscore)
                    if newscore == 0:
                        return True
                    
                    if newscore < score:
                        ret = processWord(wcopy, w2, newscore)
                        if ret == True:
                            return True
                        
            return False
                    
        """
        #print(w1, w2)
        return processWord(w1, w2, dScore(w1, w2))

        
            
            