class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        # pfx[i] = sum(nums[0:i])
        pfx = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            pfx[i] = pfx[i-1] + nums[i]

        # sfx[i] = sum(nums[i:])
        sfx = [nums[-1]] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            sfx[i] = sfx[i+1] + nums[i]

        # pivot idx is where sum(nums[0:i]) == sum(nums[i:])
        for i in range(len(nums)):
            if pfx[i] == sfx[i]:
                return i
        
        return -1 