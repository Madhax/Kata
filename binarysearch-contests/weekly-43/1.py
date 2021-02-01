class Solution:
    def solve(self, contacts):
        seen = set()
        unique = 0
        for contact in contacts:
            if len(set(contact) & seen) == 0:
                unique+=1
            seen |= set(contact)
            
                
        return unique