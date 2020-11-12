class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        """
        For each point we assert that 2 sides are equal. Given one side that has 2 equal points
        assert that each other point has 2 distances of that size
        """
       
        def dist(p1, p2):
            return sqrt((p2[0]-p1[0])**2 + (p2[1] - p1[1])**2)
       
        d1, d2, d3 = dist(p1, p2), dist(p1, p3), dist(p1, p4)
        if d1 == d2:
            equalSide = d1
            nonEqual = d3
        elif d1 == d3:
            equalSide = d1
            nonEqual = d2
        elif d2 == d3:
            equalSide = d2
            nonEqual = d1
        else:
            return False
       
        #print(d1, d2, d3)
       
        d1 = [dist(p2, p1), dist(p2, p3), dist(p2, p4)]
        #print(d1)
        if d1.count(equalSide) < 2:
            return False
        elif d1.count(nonEqual) != 1:
            return False
       
       
       
        d1 = [dist(p3, p2), dist(p3, p1), dist(p3, p4)]
        #print(d1)
        if d1.count(equalSide) < 2:
            return False
        elif d1.count(nonEqual) != 1:
            return False
       
       
        d1 = [dist(p4, p2), dist(p4, p1), dist(p4, p3)]
        #print(d1)
        if d1.count(equalSide) < 2:
            return False
        elif d1.count(nonEqual) != 1:
            return False
       
       
       
        return True
