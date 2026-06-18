class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        r = k%length
        # compute idx from where to begin rotation
        j = length - r
        
        # store elements that we are going to rotate
        temp = nums[j:]
        # push first part of elements forward
        for i in range(length-(r+1), -1, -1):
            nums[i+r] = nums[i]
        print(nums)
        # insert the other elements
        for i in range(r):
            nums[i] = temp[i]
        