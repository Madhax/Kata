import heapq
from collections import defaultdict

adj_list = defaultdict(list)
for u,v,w, in flights:
    adj_list[u].append((v,w))

pq = [(0, -1, src)]

while pq:
    cost, steps, node = heapq.heappop(pq)

    if steps>k:
        continue
    if node == dst:
        return cost

    for neighb, weight in adj_list[node]:
        heapq.heappush(pq, (cost+weight, steps+1, neighb))

        

return -1