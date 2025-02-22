class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort(key = lambda i: i[0])
        res = []

        for start,end in intervals:
            if res == []:
                res.append([start,end])
                continue
            cur_end = res[-1][1]

            if (start <= cur_end):
                res[-1][1] = max(cur_end, end)
            else:
                res.append([start,end])

        return res