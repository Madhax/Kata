class Solution:
    def beautySum(self, s: str) -> int:
        
        freq = Counter()
        for c in s:
            freq[c] += 1
            
        output = 0
        newfreq = freq.copy()
        for i in range(len(s)):
            if i > 0:
                newfreq[s[i-1]] -= 1
            innerfreq = newfreq.copy() 
            for j in range(len(s) , i, -1):
                if j <= len(s) - 1:
                    innerfreq[s[j]] -= 1
                    
                #print(s[i:j])
                #print(innerfreq.most_common(1))
                cands = [x for x in innerfreq.values() if x > 0]
                cands.sort()
                
                mostCommon = cands[-1]
                leastCommon = cands[0]
                #print(mostCommon, leastCommon)
                if leastCommon > 0 and mostCommon-leastCommon > 0:
                    output += mostCommon-leastCommon 
        
        return output