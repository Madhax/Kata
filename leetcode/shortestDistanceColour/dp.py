from functools import lru_cache


class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        
        @lru_cache(maxsize=None)
        def _distance(index, color):
            left = index
            right = index
            
            while colors[left] != color and colors[right] != color:
                if left != 0:
                    left -= 1
                
                if right != len(colors) - 1:
                    right += 1
                    
                if left == 0 and right == len(colors) - 1:
                    break
            
            if colors[left] == color:
                return index - left
            elif colors[right] == color:
                return right - index
            else:
                return -1
            
        return [_distance(q[0], q[1]) for q in queries]