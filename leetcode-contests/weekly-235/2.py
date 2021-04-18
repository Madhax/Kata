class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        
        output = [0 for x in range(k)]
        
        uam = defaultdict(set)
        
        for user, time in logs:
            uam[user].add(time)
            
        for user in uam.keys():
            output[len(uam[user])-1] += 1
            
        return output
