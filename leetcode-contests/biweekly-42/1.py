from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)
        
        didntTake = 0
        while len(sandwiches) >= 0:
            if sandwiches[0] == students[0]:
                sandwiches.popleft()
                students.popleft()
                didntTake = 0
                
            else:
                
                students.append(students.popleft())
                didntTake += 1
                
            if didntTake == len(sandwiches):
                return len(sandwiches)
        
        return 0