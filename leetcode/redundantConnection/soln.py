class DisjSet:
    def __init__(self, n):
        # Constructor to create and
        # initialize sets of n items
        self.rank = [1] * n
        self.parent = [i for i in range(n)]
  
  
    # Finds set of given item x
    def find(self, x):
          
        # Finds the representative of the set
        # that x is an element of
        if (self.parent[x] != x):
              
            # if x is not the parent of itself
            # Then x is not the representative of
            # its set,
            self.parent[x] = self.find(self.parent[x])
              
            # so we recursively call Find on its parent
            # and move i's node directly under the
            # representative of this set
  
        return self.parent[x]
  
  
    # Do union of two sets represented
    # by x and y.
    def Union(self, x, y):
          
        # Find current sets of x and y
        xset = self.find(x)
        yset = self.find(y)
  
        # If they are already in same set
        if xset == yset:
            return
  
        # Put smaller ranked item under
        # bigger ranked item if ranks are
        # different
        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
  
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
  
        # If ranks are same, then move y under
        # x (doesn't matter which one goes where)
        # and increment rank of x's tree
        else:
            self.parent[yset] = xset
            self.rank[xset] = self.rank[xset] + 1
            

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
    
        for edge in reversed(edges):
            testg = DisjSet(len(edges)+1)
            for edge2 in edges:
                if edge == edge2:
                    continue
                    
                testg.Union(edge2[0], edge2[1])
                
            if testg.find(edge[0]) == testg.find(edge[1]):
                return edge
                    
            
        