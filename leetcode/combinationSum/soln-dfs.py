class Solution:
    output = []
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = list(set(candidates))
        candidates.sort()
        currentList = []
        self.output = []
        
        def dfs(candidates, target, currentList, offset):
            
            if target == 0:
                #print(currentList)
                self.output.append(currentList.copy())
            
            if candidates[offset] > target:
                return
            
            for x in range(offset, len(candidates)):
                if candidates[x] > target:
                    return  
                
                currentList.append(candidates[x])
                dfs(candidates, target-candidates[x], currentList, x)
                currentList.pop()
                
        dfs(candidates, target, currentList, 0)
        
        return self.output
    
        