class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res, heap = [], []
        l = len(nums)

        # add first k-1 elements
        for i in range(k-1):
            heapq.heappush(heap, (-nums[i], i))

        # we begin with searching at the kth element or the (k-1)th index
        right = k-1

        # search all valid windows
        while right < l:
            # add new element
            heapq.heappush(heap, (-nums[right], right))

            # remove any elements that are outside of our window
            while heap[0][1] < (right - k + 1):
                heapq.heappop(heap)
            
            # take the max
            res.append(-heap[0][0])

            # new window
            right += 1

            
        return res

            


