"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        # we can maintain a heap where the top of the heap contains the earliest end date
        # if a new interval overlaps with the earliest end date then we need a new room

        intervals.sort(key = lambda x:x.start)

        heap = []

        for interval in intervals:
            if heap and heap[0] <= interval.start:
                heapq.heappop(heap)
            
            heapq.heappush(heap, interval.end)


        return len(heap)