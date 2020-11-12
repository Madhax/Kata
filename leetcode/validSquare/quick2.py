class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        # distance between 2 points
        def dist(p1, p2):
            return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
    
	    # all possible lines
        l = sorted([dist(p1,p2),dist(p1,p3),dist(p1,p4),dist(p2,p3),dist(p2,p4),dist(p3,p4)])
    
	    # check 4 equal sides & 2 equal diagonals
        return l[0]==l[1]==l[2]==l[3] and l[3]!=l[4] and l[4]==l[5]
    