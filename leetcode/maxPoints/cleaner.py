class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        
        slope_dict = defaultdict(set)
        for i, p1 in enumerate(points[:-1]):
            for p2 in points[i+1:]:
                if p1[0] == p2[0]:
                    a = None
                    b = p1[0]
                else:
                    a = (p2[1] - p1[1]) / (p2[0] - p1[0])
                    b = p1[1] - a * p1[0]
                slope_dict[(a,b)].update({tuple(p1), tuple(p2)})
        
        return max([len(v) for v in slope_dict.values()])
        