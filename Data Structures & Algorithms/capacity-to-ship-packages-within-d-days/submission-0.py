class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        # if len(weights) > len(days):
            # we have to ship more than 1 weight per day
        
        # the capacity is bounded below by the heaviest weight
        # the capacity is bounded above by the sum of the weights

        low = max(weights)
        high = sum(weights)

        # we have this range [low, high] and we need to find a value in it
        # binary search

        def is_valid(capacity):
            needed_days = 0
            curr = 0
            i = 0

            while i < len(weights):
                curr += weights[i]
                if curr > capacity:
                    needed_days += 1
                    curr = weights[i]
                i += 1
            return needed_days < days

        while low < high:
            mid = (low + high) // 2

            # if mid is a valid capacity then decrease high
            if is_valid(mid):
                high = mid
            # else (mid is not a valid capacity, inrease high)
            else:
                low = mid+1
            
        return low