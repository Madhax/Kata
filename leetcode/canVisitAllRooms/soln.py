class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
       
        def bfs():
           
            seen = set()
            seen.add(0)
            q = []
            q.append(0)
            while len(q) > 0:
                room = q.pop()
               
                for key in rooms[room]:
                    if key in seen:
                        continue
                    else:
                        q.append(key)
                        seen.add(key)
               
            return len(seen) == len(rooms)
       
        return bfs()
