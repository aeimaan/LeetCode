class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        latest_time = max(map(max, intervals)) + 1

        res = [0]  * latest_time

        for start, end in intervals:
            for i in range(start, end):
                res[i] += 1

        return max(res)

        