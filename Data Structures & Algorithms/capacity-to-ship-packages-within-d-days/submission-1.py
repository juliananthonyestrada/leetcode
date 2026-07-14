class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        # the capacity is bounded below by the heaviest weight
        # the capacity is bounded above by the sum of the weights
        # we have this range [low, high] and we need to find a value in it
        # binary search

        low = max(weights)
        high = sum(weights)


        def is_valid(capacity):
            needed_days, curr_weight = 0, 0

            for w in weights:
                if curr_weight+w > capacity:
                    needed_days += 1
                    curr_weight = w
                else:
                    curr_weight += w

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