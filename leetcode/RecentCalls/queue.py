class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        queue = self.queue
        while queue and queue[0] < t - 3000:
            queue.popleft()
        queue.append(t)
        return len(queue)