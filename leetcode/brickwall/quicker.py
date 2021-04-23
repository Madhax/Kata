class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        dic = collections.defaultdict(int)
        
        for row in wall:
            cur_sum = 0
            for brick in row[:-1]:
                cur_sum += brick
                dic[cur_sum] += 1
        return len(wall) - max(dic.values(),default=0)
        