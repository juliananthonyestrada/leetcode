class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = (len(nums)) - (k%len(nums))

        nums[:] = nums[j:] + nums[0:j]