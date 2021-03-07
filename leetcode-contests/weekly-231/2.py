class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        
        curSum = sum(nums)
        
        if curSum > goal:
            diff = curSum - goal
            #print(goal, curSum, diff)
            return ceil(diff/(limit))
        
        else:
            diff = goal - curSum
            #print(goal, curSum)
            return ceil(diff/(limit))
            