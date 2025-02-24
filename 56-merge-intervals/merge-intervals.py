class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key = lambda i : i[0])

        for i in range(len(intervals)):
            cur_start, cur_end = intervals[i] 
            if i == 0:
                res.append([cur_start, cur_end])
                continue
            
            merged_end = res[-1][1]

            if cur_start <= merged_end:
                res[-1][1] = max(merged_end, cur_end)
            else:
                res.append([cur_start,cur_end])

        return res