class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        smallest_end = intervals[0][1]
        
        for start, end in intervals[1:]:
            if smallest_end > start:
                res += 1
                smallest_end = min(smallest_end, end)
            else:
                smallest_end = end
        return res

        
