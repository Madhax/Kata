class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        #tuple (diffs, denominator)
        
        #negative priority queue on diff increases
        
        negHeap = []
        
        for curclass in classes:
            diff1 = curclass[0] / curclass[1]
            diff2 = (curclass[0]+1) / (curclass[1]+1)
            
            heappush(negHeap, (-abs(diff1-diff2), curclass[0], curclass[1]))

            
        while extraStudents > 0:
            
            (val, num, denom) = heappop(negHeap)
            
            num += 1
            denom += 1
            
            diff1 = num/denom
            diff2 = (num+1)/(denom+1)
            
            heappush(negHeap, (-abs(diff1-diff2), num, denom))
            
            extraStudents -= 1
            
        
        average = 0
        
        while len(negHeap) > 0:
            (val, num, denom) = heappop(negHeap)
            
            average += num/denom
            
        return average/len(classes)