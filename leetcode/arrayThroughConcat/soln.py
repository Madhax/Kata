class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        
        def listCompare(index, choice):
            nonlocal arr
            for offset, piece in enumerate(choice):
                #print(offset, piece)
                try:
                    if arr[index+(offset)] != piece:
                        return False
                except:
                    return False
                
            #print("here")
            return True
            
        
        def dfs(index, choiceSet):
            nonlocal arr
            
            if index == len(arr):
                return True
            
            for iter in range(len(choiceSet)):
                if listCompare(index, choiceSet[iter]):
                    chosen = choiceSet.pop(iter)
                    
                    retVal = dfs(index+len(chosen), choiceSet)
                    #print(retVal)
                    if retVal == True:
                        return True
                    
                    choiceSet.insert(iter, chosen)
            
            return False
        
        
        return dfs(0, pieces)