class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []
        def isPalindrome(val):
            for x in range(0, len(val) // 2):
                if val[x] != val[(x+1) *-1]:
                    return False
            return True
        
        def buildPartitions(s, currentSet, index):
            nonlocal output
            #print(s, currentSet, index)
            if index == len(s):
                output.append(currentSet.copy())
                
            for x in range(index+1, len(s)+1):
                
                if isPalindrome(s[index:x]):
                    currentSet.append(s[index:x])
                    buildPartitions(s, currentSet, x)
                    currentSet.pop()
                    
        buildPartitions(s, [], 0)
        return output
                