class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # key insight multiple subarrays can have the same sum i.e. multiple elements of 
        # prefix will have the same value - instead of recomputing them
        # why not store their frequencies in a map

        res, curr_sum = 0, 0
        freq_map = {0 : 1}

        for num in nums:
            curr_sum += num
            diff = curr_sum - k

            res += freq_map.get(diff, 0)
            freq_map[curr_sum] = 1 + freq_map.get(curr_sum, 0)
            
        return res