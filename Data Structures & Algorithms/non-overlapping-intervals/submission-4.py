class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        if not intervals:
            return 0

        res = 0
        intervals.sort()
        smallest_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if smallest_end > intervals[i][0]:
                res += 1
                smallest_end = min(smallest_end, intervals[i][1])
            else:
                smallest_end = intervals[i][1]
        return res

        
