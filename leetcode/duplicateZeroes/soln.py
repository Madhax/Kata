class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        x = 0
        startLen = len(arr)
        while x < len(arr):
            if arr[x] == 0:
                arr[:] = arr[0:x] + [0] + arr[x:]
                x += 1
            x += 1
        
        arr[:] = arr[:startLen]
        #print(arr)