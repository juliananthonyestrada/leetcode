class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        
        i, j = 0, 0

        slots1.sort()
        slots2.sort()

        while i < len(slots1) and j < len(slots2):
            start1, end1 = slots1[i][0], slots1[i][1]
            start2, end2 = slots2[j][0], slots2[j][1]

            later_start = max(start1, start2)
            earlier_end = min(end1, end2)

        # overlap
            if later_start < earlier_end:
                if earlier_end - later_start >= duration:
                    return [later_start, later_start + duration]
        
        # no overlap - advance 
            if end1 < end2:
                i += 1
            else:
                j += 1

        return []