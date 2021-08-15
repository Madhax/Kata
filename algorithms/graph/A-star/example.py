import heapq

#euclidean
def heuristic(a,b):
    return (b[0]-a[0]) ** 2 + (b[1]-a[1]) ** 2

#manhattan
def heristic2(a,b):
    return abs(b[0]-a[0]) + abs(b[1]-a[1])

def astar(array, start, goal):

    returnPath = {}
    visited = set()

    gscore = {start:0}
    fscore = {start: heuristic(start, goal)}

    pq = []

    heappush(pq, (fscore[start], start))
    
    while pq:

        _, current = heappop(pq)
        #build path
        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]

            return data

        visited.add(current)

        for i, j in neighbors:

            neighbor = current[0] + i, current[1] + j

            tentative_score = gscore[current] + heuristic(current, neighbor)

            if 0 <= neighbor[0] < N and 0 <= neighbor[1] < M and array[neighbor[0]][neighbor[1]] == 0:
                if neighbor in close_set and tentative_score >= gscore.get(neighbor, 0):
                    continue

            
            if tentative_score < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in pq]:
                came_from[neighbor] = current
                #gscore[neighbor] = tentative_score
                fscore[neighbor] = tentative_score + heuristic(neighbor, goal)
                heappush(pq, (fscore[neighbor], neighbor))

    
    return False