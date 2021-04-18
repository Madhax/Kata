class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        
        currentSum = 0
        
        sortedNums = list(set(nums1))
        sortedNums.sort()
        
        bestIndex = None
        bestDiff = -math.inf
        bestVal = None
        for x in range(len(nums1)):
            significantVal = abs(nums1[x] - nums2[x])
            currentSum += significantVal
            
            #check best diff
            
            if significantVal > bestDiff:
                
                index = bisect.bisect_left(sortedNums, nums2[x])
                if index > 0 and index < len(sortedNums):
                    closest = min([sortedNums[index-1], sortedNums[index]],key=lambda lx:abs(lx-nums2[x]))
                elif index < len(sortedNums):
                    closest = sortedNums[index]
                else:
                    closest = sortedNums[index-1]

                testVal= abs(closest- nums2[x])
                
                if significantVal - testVal > bestDiff:
                    bestDiff = significantVal - testVal 
                    bestIndex = x
                    bestVal = closest
        
        #print(bestDiff, bestIndex, closest)
        
        if bestDiff > 0:
            currentSum -= abs(nums1[bestIndex] - nums2[bestIndex])
            nums1[bestIndex] = closest
            currentSum += abs(nums1[bestIndex] - nums2[bestIndex])
        return currentSum % (10**9 + 7)