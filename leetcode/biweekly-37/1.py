class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arrLen = len(arr)
        remove = ceil(arrLen/10/2)
        arr.sort()
        arr = arr[remove:-remove]
        return sum(arr)/len(arr)