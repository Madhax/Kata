class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        def mine():
            '''
            Eliminate shorter or earlier terminating buildings than the previous
            because they will not contribute to the skyline
            '''
            filtered = []
            left, right, height = 0, 1, 2
            for building in buildings:
                if not filtered:
                    filtered.append(building)
                    continue
                #check whether current building is taller and wider than previous
                if building[height] > filtered[-1][height] or \
                    building[right] > filtered[-1][right]:
                    filtered.append(building)
            
            x_heights = [] #x, height
            #save (left, -height) and (right, height) as tuples into x_heights
            for building in filtered:
                heappush(x_heights, (building[left], -building[height]))
                heappush(x_heights, (building[right], building[height]))
            
            result = []
            heights, prev = [0], 0
            while x_heights:
                x, height = heappop(x_heights)
                if height < 0: #left edge, so insert in it's place
                    bisect.insort(heights, -height)
                else: #right edge, so pop it out
                    ix = bisect.bisect_left(heights, height)
                    del heights[ix]
                
                if heights[-1] != prev: #max height has changed
                    result.append((x, heights[-1]))
                    prev = heights[-1]
                
            return result
        return mine()
