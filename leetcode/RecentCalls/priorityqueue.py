import heapq
class RecentCounter:

    def __init__(self):
        self.priority = []

    def ping(self, t: int) -> int:
        heapq.heappush(self.priority, t)
        EarliestTime = t - 3000
        while len(self.priority) > 0 and self.priority[0] < EarliestTime:
            heapq.heappop(self.priority)

        return len(self.priority)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)