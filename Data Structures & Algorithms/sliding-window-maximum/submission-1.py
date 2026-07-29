class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []
        heap = []
        l = len(nums)
        for i in range(k-1):
            heapq.heappush(heap, (-nums[i], i))

        right = k-1

        while right < l:
            heapq.heappush(heap, (-nums[right], right))

            # remove any elements that are outside of our window
            while heap[0][1] < (right - k + 1):
                heapq.heappop(heap)
            
            res.append(-heap[0][0])

            right += 1

            
        return res

            


