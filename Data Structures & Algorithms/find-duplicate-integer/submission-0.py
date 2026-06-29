class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # trivial solution using linear space
        # build a seen set, if seen return it, else, add to set

        seen = set()

        for num in nums:
            if num in seen:
                return num
            else:
                seen.add(num)