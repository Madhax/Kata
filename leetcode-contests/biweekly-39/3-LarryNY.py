class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        
        queue = collections.deque()
        
        queue.append((0, 0, 0))
        seen = set()
        forb = set(forbidden)
        
        while len(queue) > 0:
            d, now, used = queue[0]
            queue.popleft()
            
            #print(queue, d, now, used)
            if now == x:
                return d
            
            if now + a not in forb and now + a - b - b <= 4000 and (now + a, False) not in seen:
                queue.append((d + 1, now + a, False))
                seen.add((now + a, False))
                
            if now - b not in forb and now - b >= 0 and not used and (now - b, used) not in seen:
                queue.append((d + 1, now - b, True))
                seen.add((now - b, True))

        return -1
            
        
