class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # edge case: empty array
        if not nums:
            return 0
        # convert to a set for O(1) lookup
        nums = set(nums)
        longest = 1

        for n in nums:
            curr = 1
            # we found the start of a sequence
            if n-1 not in nums:
                i = 1
                # count the sequence
                while n+i in nums:
                    curr += 1 
                    i += 1
                # update longest
                longest = max(curr, longest)

        return longest

