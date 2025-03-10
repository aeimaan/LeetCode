class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key= lambda i : i[0])
        
        prevEnd = -1
        for beg, end in intervals:
            if beg < prevEnd:
                return False
            prevEnd = end
        return True