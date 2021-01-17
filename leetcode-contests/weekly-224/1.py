class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        arr = [min(x,y) for x, y in rectangles]
        return arr.count(max(arr))