"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        self.ids = {}
                
        def getScore(node):
            score = node.importance
            for sub in node.subordinates:
                score += getScore(self.ids[sub])
                
            return score
        
        for emp in employees:
            self.ids[emp.id] = emp
            
        return getScore(self.ids[id])