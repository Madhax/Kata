class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        
        seats.sort()
        students.sort()
        
        cost = 0
        
        for s1, s2 in zip(seats, students):
            cost += abs(s1-s2)
            
        return cost
