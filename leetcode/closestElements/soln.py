class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        workList = []
        for val in arr:
            workList.append((abs(val-x), val))
        
        workList.sort()
        #print(workList)
        output = [x for _, x in workList[:k]]
        output.sort()
        return output
    