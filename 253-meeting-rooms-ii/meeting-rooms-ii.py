class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i : i[0])
        heap = []

        heapq.heappush(heap, intervals[0][1]) # push onto it current end time

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if heap[0] <= start:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
        return len(heap)
        
