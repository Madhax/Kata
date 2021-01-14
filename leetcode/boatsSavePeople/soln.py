class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
       
        i, j = 0, len(people)-1
        output = 0
        while i <= j:
            if people[i] + people[j] > limit:
                output += 1
                j -= 1
               
            else:
                output += 1
                j-= 1
                i += 1
               
        return output
