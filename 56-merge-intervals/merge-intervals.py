class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort(key = lambda i : i[0])
        res = [intervals[0]]

        for i in range(1 , len(intervals)):
            start, end = res[-1][0], res[-1][1]
            next_start, next_end = intervals[i][0], intervals[i][1]

            if next_start <= end or next_start == start:
                res[-1] = [start, max(end,next_end)]
            else:
                res.append(intervals[i])

        return res