import functools
from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        #assert sorted sets equal
        s1 = set(word1)
        s2 = set(word2)
        if s1 != s2:
            print("here")
            return False
        
        counter1 = Counter()
        counter2 = Counter()
        
        for c in word1:
            counter1[c] += 1
        
        for c in word2:
            counter2[c] += 1
            
        l1 = list(counter1.values())
        l1.sort()
        l2 = list(counter2.values())
        l2.sort()

        
        return l1 == l2
        #assert sorted frequencies equal
        
        