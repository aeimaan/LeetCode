class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        intervals.sort(key = lambda i : i[0])
        heapq.heappush(heap, intervals[0][1]) # throw 1st end time onto the queue

        for i in intervals[1:]:
            start = i[0]

            if heap[0] <= start:
                heapq.heappop(heap)
            
            heapq.heappush(heap, i[1])

        return len(heap)

        
