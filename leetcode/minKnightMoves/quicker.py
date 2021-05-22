class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
            return 0
        
        # greedy
        x, y = abs(x), abs(y)
        res = 0
        while x > 4 or y > 4:
            res += 1
            if x >= y:
                x -= 2
                y -= 1 if y >= 1 else -1
            else:
                x -= 1 if x >= 1 else -1
                y -= 2

        moves = [(1, 2), (2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1), (-1, 2), (-2, 1)]
        visited = set()
        queue = [(0, 0, 0)]
        min_steps = 9999
        while queue:
            curr_x, curr_y, steps = queue.pop(0)
            
            if curr_x == x and curr_y == y:
                return res + steps
            
            for move in moves:
                next_x, next_y = curr_x + move[0], curr_y + move[1]
                if (next_x, next_y) not in visited:
                    visited.add((next_x, next_y))
                    queue.append((next_x, next_y, steps + 1))
                