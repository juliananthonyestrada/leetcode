class Solution:
    import math
    import heapq
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # create a min heap
        # what we compare nodes on is euclidean distance to the origin
        # the root of the min heap is the point closes to the origin 
        # we will store in the min heap the distance
        # and then have a hash map -> distance : point
        res = []
        hshmp = {}

        for point in points:
            distance = math.sqrt((point[0])**2 + (point[1])**2)
            if distance in hshmp:
                hshmp[distance].append(point)
            else:
                hshmp[distance] = [point]
        
        heap = list(hshmp.keys())
        heapq.heapify(heap)

        ctr = 0
        while ctr < k:
            curr_dist = heapq.heappop(heap)
            for dist in hshmp[curr_dist]:
                res.append(dist)
                ctr += 1

        return res