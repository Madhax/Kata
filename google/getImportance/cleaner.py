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
        
        emp = {e.id:e for e in employees}
        stack = [emp[id]]
        total_imp = 0
        while stack:
            e = stack.pop()
            total_imp+=e.importance
            for s in e.subordinates:
                stack.append(emp[s])
        return total_imp
        
        