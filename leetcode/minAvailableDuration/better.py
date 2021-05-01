class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        heap = []
        for start, end in slots1:
            if end - start >= duration:
                heapq.heappush(heap, (start, end))
        
        for start, end in slots2:
            if end - start >= duration:
                heapq.heappush(heap, (start, end))
        
        while len(heap) > 1:
            first_start, first_end = heapq.heappop(heap)
            second_start, second_end = heap[0]
            if second_start >= first_end:
                continue
            end = min(first_end, second_end)
            if end - second_start >= duration:
                return [second_start, second_start + duration]
        
        return []