class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i: i[0])
        heap = []
        # heapq.heappush(heap, intervals[0][1])

        for start, end in intervals:
            if not heap:
                heapq.heappush(heap, end)
                continue
            if start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
        return len(heap)
