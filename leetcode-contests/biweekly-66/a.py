class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        cnt = 0
        w1 = Counter(words1)
        w2 = Counter(words2)
        
        for word in w1.keys():
            if w1[word] == 1 and w2[word] == 1:
                cnt += 1
        
        return cnt