class Solution:
    maxValue = 0
    bestPath = None
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        d = {}
        v = {}
        allNodes = set()
        
        for p1, p2 in roads:
            if p1 not in d:
                d[p1] = 1
                v[p1] = [p2]
            else:
                d[p1] += 1
                v[p1].append(p2)
            
            if p2 not in d:
                d[p2] = 1
                v[p2] = [p1]
            else:
                d[p2] += 1
                v[p2].append(p1)
            
            allNodes.add(p1)
            allNodes.add(p2)
            
            
        maxNetwork = 0
        
        for node in allNodes:
            for node2 in allNodes:
                if node == node2:
                    continue
                
                val = d[node] + d[node2]
                if node in v[node2]:
                    val -= 1
                
                if val > maxNetwork:
                    maxNetwork = val
                
        #print(self.bestPath)
        return maxNetwork