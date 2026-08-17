class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        res = 0
        intervals.sort()
        left, right = 0, 1

        while right < len(intervals):
            left_strt, left_end = intervals[left][0], intervals[left][1]
            right_strt, right_end = intervals[right][0], intervals[right][1]

            # overlap exists
            if left_end > right_strt:
                res += 1

                if left_end > right_end:
                    intervals.remove(intervals[left]) 
                else:
                    intervals.remove(intervals[right])
            # no overlap
            else:
                left += 1
                right += 1
        
        return res