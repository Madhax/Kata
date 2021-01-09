class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        canRemove = True
       
        #while canRemove:
        for piece in pieces:
            if any(piece == arr[i:i+len(piece)] for i in range(len(arr))):
                arr = [x for x in arr if x not in piece]
               
            if len(arr) == 0:
                return True
               
        return False