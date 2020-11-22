class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        energies = sorted(tasks, key = lambda x : x[0]-x[1])
        
        @lru_cache(maxsize=None)
        def canFinish(index, remainingEnergy):
            nonlocal energies
            if index == len(energies):
                return remainingEnergy
            elif remainingEnergy < energies[index][1]:
                return -1
            else:
                return canFinish(index+1, remainingEnergy-energies[index][0])
            
        #bsearch for ideal energy
        
        high = sum(x[1] for x in energies)
        low = max(max(x[1] for x in energies), sum(x[0] for x in energies)) 
        
        #print(energies)
        #print(canFinish(0, 32))
        #print(high, low)
        mid = floor((high - low)/2) + low
        lowestFound = float("inf")
        while True:
            
            rem = canFinish(0, mid)
            if rem >= 0:
                lowestFound = mid
                high = mid
                newmid = floor((high - low)/(log(rem+1) + 2)) + low
                if newmid == mid:
                    break
                mid = newmid
                
            else:
                low = mid
                newmid = floor((high - low)/2) + low
                if newmid == mid:
                    break
                mid = newmid
                
            
        return lowestFound