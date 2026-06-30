"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        # conflict when int1[end] > int2[start]

        if len(intervals) < 2:
            return True

        intervals = sorted(intervals, key = lambda iv : iv.start)
        
        i1, i2 = 0, 1

        while i2 < len(intervals):
            if intervals[i1].end > intervals[i2].start:
                return False
            i1 += 1
            i2 += 1

        return True