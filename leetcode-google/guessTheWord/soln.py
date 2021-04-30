# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        
        @functools.cache
        def dist(w1, w2):
            sim = 0
            for c1, c2 in zip(w1, w2):
                if c1 == c2:
                    sim += 1
                    
            return sim
        
        def buildHeap(wl):
            h = []
            for y in range(len(wl)):
                score = 0
                for x in range(len(wl)):
                    if y == x:
                        continue
                    score += dist(wl[y], wl[x])
                    
                heappush(h, (-score, wl[y]))
            
            return h
                    
        
        pq = buildHeap(wordlist)
        
        iter = 0
        while iter <= 10:
            similarity = master.guess(pq[0][1])
            wordlist = [x for x in wordlist if dist(x, pq[0][1]) == similarity]
            if len(wordlist) == 1:
                master.guess(wordlist[0])
                ##print(wordlist[0])
                return 0
            pq = buildHeap(wordlist)
            
            iter += 1
            #print(len(wordlist))
        
        return 0 
                